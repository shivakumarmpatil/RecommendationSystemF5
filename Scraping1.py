# -*- coding: utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup
lst_Price = []
lst_Beds = []
lst_Baths = []
lst_Area = []
lst_Street = []
lst_City = []
lst_Region = []
lst_Zip = []
lst_Pets = []
for index in range(100):
    try:
        page = requests.get('https://www.realtor.com/apartments/New-York_NY/pg-'+str(index))
        soup = BeautifulSoup(page.text, 'html.parser')
    except:
        print("Page retrieval issue")    
    
    for l in soup.findAll('li', { 'class' : 'component_property-card'}):
        try:
            lst_Price.append(l.find('span',{'class':'data-price'}).text)
        except:
            lst_Price.append("Data Not Found")
        try:     
            lst_Street.append(l.find('span',{'class':'listing-street-address'}).text)
        except:
            lst_Street.append("Data Not Found")
        try:
            lst_City.append(l.find('span',{'class':'listing-city'}).text)
        except:
            lst_City.append("Data Not Found")
        try:
            lst_Region.append(l.find('span',{'class':'listing-region'}).text)
        except:
            lst_Region.append("Data Not Found")
        try:
            lst_Zip.append(l.find('span',{'class':'listing-postal'}).text)
        except:
            lst_Zip.append("Data Not Found")
        try:
            lst_Beds.append(l.find('li',{'data-label':'property-meta-beds'}).text)
        except:
            lst_Beds.append("Data Not Found")
        try:
            lst_Baths.append(l.find('li',{'data-label':'property-meta-baths'}).text)
        except:
            lst_Baths.append("Data Not Found")
        try:
            lst_Area.append(l.find('li',{'data-label':'property-meta-sqft'}).text)
        except:
            lst_Area.append("Data Not Found")
        try:
            lst_Pets.append(l.find('li',{'data-label':'property-meta-pets'}).text)
        except:
            lst_Pets.append("NO")
        
    strt = [i.replace('\n','') for i in lst_Street]
    new_street=[]
    for s in strt:
        new_street.append(s.lstrip())

        
df = pd.DataFrame({'Price':lst_Price,'Beds':lst_Beds,'Baths':lst_Baths,'Area':lst_Area,'Pets':lst_Pets,'Street':new_street,'City':lst_City,'Region':lst_Region,'Zip':lst_Zip})
df.to_csv('Apartments1.csv', index=False)
