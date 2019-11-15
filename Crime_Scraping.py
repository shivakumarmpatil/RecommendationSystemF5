# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:22:03 2019

@author: LenovoFlex
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup


try:
    page = requests.get('https://spotcrime.com/ny/brooklyn')
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find("table",attrs ={"class":"table-crime-data"})
    headings = []
    
    headings = [th.get_text() for th in table.find("tr").find_all("th")]
    
except:
    print("Page retrieval issue")  
data=[]
datasets = []
counter =1
heads = []
for row in table.findAll("tr"):
    heads.append(row.find("th").getText())
    try:
        for s in row.findAll("td"):
            if counter == 4:
                print(heads)print(s.getText())
                counter = 1
            else:
                counter +=1
    except:
        print("err")
            
