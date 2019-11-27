# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:29:27 2019

@author: user
"""

import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

df1 = pd.read_csv("cleanest.csv")
df1.drop_duplicates(subset =["Price","Beds","Baths","Street"],keep = 'first', inplace = True) 
df1.to_csv("Data_v1.csv")
a= df1.Zip.unique()
unique_zip={}
count = 0.001
for u in range(len(a)):
    count = round(count,3)
    unique_zip[a[u]]=count
    count+= 0.001

df1['Pets'] = df1['Pets'].replace('No', 0) 
df1['Pets'] = df1['Pets'].replace('Yes', 1) 
x,y=[],[]

for index, row in df1.iterrows():
    price = row['Price'].replace(',','')
    area = row['Area'].replace(',','')
    for key,value in unique_zip.items():
        if key == row['Zip']:
            x.append([row['Beds'],row['Baths'], row['Pets'],int(area),value])
            y.append(int(price))
            break
       
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5,random_state=1)
reg = LinearRegression() 
reg.fit(x_train, y_train)

print('Coefficients: \n', reg.coef_) 
print(reg.score(x_test, y_test))
prediction = reg.predict(x_test)
area_prediction,price_prediction,bed_prediction,bath_prediction,pet_prediction,zip_prediction = [],[],[],[],[],[]
for i in range(len(prediction)):
    for key, value in unique_zip.items(): 
         if  x_test[i][4] == value: 
             
            bed_prediction.append(x_test[i][0])
            bath_prediction.append(x_test[i][1])
            pet_prediction.append(x_test[i][2])
            area_prediction.append(x_test[i][3])
            zip_prediction.append(key)
            price_prediction.append(prediction[i])
    
linearmodel=pd.DataFrame({'Bed':bed_prediction, 'Bath': bath_prediction, 'Pet':pet_prediction,'Zip':zip_prediction, 'Area': area_prediction, 'Price': price_prediction})
linearmodel.to_csv("Linearmodel.csv")