# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:22:03 2019

@author: LenovoFlex
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup
headings = []
full_df =pd.DataFrame() #pd.DataFrame({'City','Theft', 'Robbery', 'Burglary', 'Vandalism', 'Shooting', 'Arson', 'Arrest', 'Assault', 'Other'})
ind = 0
city_bor = ['bronx','manhattan','queens','brooklyn','statenisland']

for ind in range(5):
    try:
        page = requests.get('https://spotcrime.com/ny/'+city_bor[ind])
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find("table",attrs ={"class":"table-crime-data"})
    except:
        print("Page retrieval issue")  
    data=[]
    datasets = []
    counter =1
    heads = []
    c_values = []
    for row in table.findAll("tr"):
        heads.append(row.find("th").getText())
        try:
            for s in row.findAll("td"):
                if counter == 4:
                    c_values.append(s.getText())
                    counter = 1
                else:
                    counter +=1
        except:
            print("err")
    df = pd.DataFrame({'City':[city_bor[ind]],str(heads[1]):[c_values[0]],str(heads[2]):[c_values[1]],str(heads[3]):[c_values[2]],str(heads[4]):[c_values[3]],str(heads[5]):[c_values[4]],str(heads[6]):[c_values[5]],str(heads[7]):[c_values[6]],str(heads[8]):[c_values[7]],str(heads[9]):[c_values[8]]})
    full_df = full_df.append(df,ignore_index = True)
    
full_df.to_csv('Crime_Stats.csv', index=False)


#print(c_values)
