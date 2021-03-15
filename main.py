from tkinter import *
import random
from PIL import ImageTk, Image
import datetime
import json

root = Tk()
root.title("Random Person Generator")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")



#converting height to centimeters and rounding to the 2nd decimal place
def height_to_centimeters(height):
    height = height.replace("'", ".")
    return str(round(float(height) * 30.48, 2))

#converting pounds to kilograms and rounding the the 2nd decimal place
def pounds_to_kilogram(weight):
    return str(round(float(weight) / 2.205, 2))

#accounting for days in a month
def february_change(month):
    if month == "February":
        return random.randint(1, 28)
    elif month == "September" or "April" or "June" or "November":
        return random.randint(1, 30)
    else:
        return random.randint(1, 31)

#clear the screen and then generate another person
def close_all():
    for widget in root.winfo_children():
        widget.grid_forget()
        widget.pack_forget()
        widget.place_forget()

    main()

#creating a json file and then exporting the data to it
def export_json(data):
    with open("Generated Data.txt", "w") as DataFile:
        json.dump(data, DataFile, indent=2)


def main():
    load = Image.open(fr"RPG\placeholder_pic.png")
    card = ImageTk.PhotoImage(load)
    img = Label(image=card)
    img.image = card
    img.grid(row=0, column=0, rowspan=3)

#reading the names in the csv file then splitting on every comma and assigning two of them to first and last names
    with open(r"RPG\name.csv", "r") as NameFile:
        EachName = NameFile.readlines()
        FirstName = random.choice(EachName).split(",")[1].replace("\n", "")
        LastName = random.choice(EachName).split(",")[1].replace("\n", "")

    Name_label = Label(root, text=f"{FirstName} {LastName}", font=("Calibri bold", 20))
    Name_label.grid(row=0, column=1)

#reading the address in the address.txt file then splits them on every comma to the the street addres and the state and area number
    with open(r"RPG\address.txt", "r") as AddressFile:
        AddressLst = AddressFile.readlines()
        Street = random.choice(AddressLst).split(",")
        State = Street[1]

    Address_label = Label(root, text=Street[0], font=("Calibri", 12))
    Address_label.grid(row=1, column=1)
    State_label = Label(root, text=State, font=("Calibri", 12))
    State_label.grid(row=2, column=1)

    PhoneNumber = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"

    phone_label = Label(root, text="PHONE:")
    phone_label.grid(row=3, column=1)

    current_phone_label = Label(root, text=PhoneNumber)
    current_phone_label.grid(row=3, column=2, padx=20)

    age_num = random.randint(18, 99)

    months = {
        "January": "Capricorn",
        "February": "Aquarius",
        "March": "Pisces",
        "April": "Aries",
        "May": "Taurus",
        "June": "Gemini",
        "July": "Cancer",
        "August": "Leo",
        "September": "Virgo",
        "October": "Libra",
        "November": "Scorpio",
        "December": "Sagittarius",
    }
    month, zodiac = random.choice(list(months.items()))

    birthyear = random.randint(1990, 2021)
    birthday = f"{month} {february_change(month)},{birthyear}"

    birthday_tag = Label(root, text="BIRTHDAY", font=("Calibri bold", 14))
    birthday_tag.grid(row=4, column=1)
    current_birthday_label = Label(root, text="Date of Birth:")
    current_birthday_label.grid(row=5, column=1)
    current_birthday = Label(root, text=birthday)
    current_birthday.grid(row=5, column=2, padx=20)

    current_year = datetime.datetime.now()
    current_year = current_year.year

    correct_age = current_year - birthyear

    current_age_label = Label(root, text="Age:")
    current_age_label.grid(row=6, column=1)
    current_age = Label(root, text=f"{correct_age} years old")
    current_age.grid(row=6, column=2)

    current_zodiac_label = Label(root, text="Zodiac")
    current_zodiac_label.grid(row=7, column=1)
    current_zodiac = Label(root, text=zodiac)
    current_zodiac.grid(row=7, column=2)

    email = f"{FirstName}{LastName}@gmail.com"

    Social_tag = Label(root, text="SOCIALS", font=("Calibri bold", 14))
    Social_tag.grid(row=8, column=1)
    current_email_label = Label(root, text="Email:")
    current_email_label.grid(row=9, column=1)
    current_email = Label(root, text=email)
    current_email.grid(row=9, column=2)

    card_lst = ["Visa:", "Mastercard:", "Discover:", "American Express:"]
    card = random.choice(card_lst)

    card_nums = f"{random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)}"
    ExperirationDate = f"{random.randint(1,12)}/{random.randint(2021,2030)}"
    CVV = random.randint(100, 999)

    finance_tag = Label(root, text="FINANCE", font=("Calibri bold", 14))
    finance_tag.grid(row=10, column=1)

    current_card_label = Label(root, text=card)
    current_card_label.grid(row=11, column=1)
    current_card_nums = Label(root, text=card_nums)
    current_card_nums.grid(row=11, column=2)
    card_expiration_date_label = Label(root, text="Expiration Date:")
    card_expiration_date_label.grid(row=12, column=1)
    card_expiration_date = Label(root, text=ExperirationDate)
    card_expiration_date.grid(row=12, column=2)
    card_cvv_label = Label(root, text="CVV:")
    card_cvv_label.grid(row=13, column=1)
    card_cvv = Label(root, text=CVV)
    card_cvv.grid(row=13, column=2)

    majors = [
        "Agriculture and Agriculture Operations",
        "Architecture and Related Services",
        "Area, Ethnic, Cultural, Gender, and Group Studies",
        "Aviation",
        "Biological and Biomedical Sciences",
        "Business, Management, Marketing, and Related Support Services",
        "Communication, Journalism, and Related Programs",
        "Communications Technologies/technicians and Support Services",
        "Computer and Information Sciences and Support Services",
        "Construction Trades",
        "Education",
        "Engineering Technologies and Engineering-Related Fields",
        "Engineering",
        "English Language and Literature/letters",
        "Family and Consumer Sciences/human Sciences",
        "Foreign Languages, Literatures, and Linguistics",
        "Health Professions and Related Programs",
        "History",
        "Homeland Security, Law Enforcement, Firefighting",
        "Human Services",
        "Legal Professions and Studies",
        "Liberal Arts and Sciences Studies and Humanities",
        "Library Science",
        "Mathematics and Statistics",
        "Mechanic and Repair Technologies/technicians",
        "Military Technologies and Applied Sciences",
        "Multi/interdisciplinary Studies",
        "Natural Resources and Conservation",
        "Parks, Recreation, Leisure, and Fitness Studies",
        "Personal and Culinary Services",
        "Philosophy and Religious Studies",
        "Physical Sciences",
        "Precision Production",
        "Psychology",
        "Science Technologies/technicians",
        "Social Sciences",
        "Theology and Religious Vocations",
        "Transportation and Materials Moving",
        "Visual and Performing Arts",
    ]

    major = random.choice(majors)

    major_tag = Label(root, text="EMPLOYMENT", font=("Calibri bold", 14))
    major_tag.grid(row=14, column=1)
    occupation_label = Label(root, text="Occupation:")
    occupation_label.grid(row=15, column=1)
    occupation = Label(root, text=major)
    occupation.grid(row=15, column=2)

    height = f"{random.randint(4,6)}'{random.randint(0,10)}"
    centimeter = height_to_centimeters(height)

    weight = random.randint(100, 300)
    kilogram = pounds_to_kilogram(weight)

    physical_traits_tag = Label(root, text="PHYSICAL TRAITS", font=("Calibri bold", 14))
    physical_traits_tag.grid(row=16, column=1)
    height_label = Label(root, text="Height:")
    height_label.grid(row=17, column=1)
    current_height = Label(root, text=(f'{height}" ({centimeter} centimeters)'))
    current_height.grid(row=17, column=2)
    weight_label = Label(root, text="Weight:")
    weight_label.grid(row=18, column=1)
    current_weight = Label(root, text=(f"{weight} pounds ({kilogram} kilogram)"))
    current_weight.grid(row=18, column=2)


#collect data in JSON format
    data = {
        "Name": {"first": FirstName, "last": LastName},
        "address": Street,
        "phone": PhoneNumber,
        "date of birth": birthday,
        "age": correct_age,
        "zodiac": zodiac,
        "email": email,
        "finance": {
            "card": card,
            "16 digits": card_nums,
            "experiation date": ExperirationDate,
            "cvv": CVV,
        },
        "occupation": major,
        "physical traits": {"height": height, "weight": weight},
    }


    generate = Button(root, text="Generate", command=lambda: close_all())
    generate.grid(row=3, column=0)

    export_to_json = Button(root, text="Export to JSON", command=lambda: export_json(data))
    export_to_json.grid(row=4, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()