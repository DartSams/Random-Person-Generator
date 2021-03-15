from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

#goes to the website and returns the html of it
def extract(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup

#scans the html for every 'ol' tag
def transform(soup):
    name=soup.find('ol',class_='comp mntl-sc-block mntl-sc-block-html')
    filtered_name_lst=re.findall('[A-Z][^A-Z]*', name.text) #reads the names list then splits on every capital letter
    for i in filtered_name_lst:
        names.append(i)




names=[]


transform(extract('https://www.verywellfamily.com/top-1000-baby-boy-names-2757618'))

transform(extract('https://www.verywellfamily.com/top-1000-baby-girl-names-2757832'))

#using pandas to export scraped names to csv file with a column called 'Names'
a=pd.DataFrame(names)
a.columns=['Names']
a.to_csv('name.csv')

with open('name.csv','r') as f:
    print(f.readlines())
