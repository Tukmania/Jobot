from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
search='https://www.kenyajob.com/job-vacancies-search-kenya/computing'
html_text=requests.get(search).text
soup= BeautifulSoup(html_text,'lxml')
# print(soup)
jobs=soup.find_all('div',class_='job-search-result')
# print(jobs)
for job in jobs:    
    my_name=job.find_all('div',class_='row')
    description=job.find('div',class_='search-description')   
    titles=job.find('div',class_='col-lg-5 col-md-5 col-sm-5 col-xs-12 job-title')
    print(titles.h5.text)
    print('https://kenyajob.com/'+titles.h5.a['href'])
    print(description.text)
  