import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

data = pd.read_csv(r'C:\Users\user\RecommendationSystemF5-Data_sets\Data_v1.csv', header=0)
data['Price'] = data['Price'].str.replace(',','')
data = data.dropna()
data = data.drop(["Unnamed: 0","Unnamed: 0.1"],axis = 1)

data["Price"].describe()
min(data["Price"])

data['Price'] = data['Price'].astype(int)

def update_range(num):
    if num > 3000 :
        return 1

    else :
        return 0

data["Price"] = data["Price"].apply(update_range)


print(data.shape)
print(list(data.columns))
print(data.head())
plt.scatter(data.City,data.Price,marker= '+', color='red')

le = preprocessing.LabelEncoder()

le.fit(data["Zip"])
data["Zip"] = le.transform(data["Zip"])

le.fit(data["Pets"])
data["Pets"] = le.transform(data["Pets"])

data['Area'] = data['Area'].str.replace(',','').astype(int)

x_train, x_test, y_train, y_test = train_test_split(data[["Area","Zip","Beds","Baths","Pets"]],data[['Price']], test_size =0.1 )
#x_train = x_train.reshape(-1,1)
#x_test = x_test.reshape(-1,1)


print(x_test)
print(x_train)
model = LogisticRegression()
print(model.fit(x_train,y_train))
print(model.predict(x_test))
print(model.score(x_test,y_test))
print(model.predict_proba(x_test))


y_pred = model.predict(x_test)
confusion_matrix(y_test, y_pred)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

df = pd.DataFrame(data, columns = ['Price','Area', 'Zip', 'Beds', 'Baths', 'Pets'])
#print(df)
df.to_csv(r"C:\Users\user\RecommendationSystemF5-Data_sets\logi.csv")
#print("Precision:",metrics.precision_score(y_test, y_pred))
#print("Recall:",metrics.recall_score(y_test, y_pred))

