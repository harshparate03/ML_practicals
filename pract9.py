import pandas as pd
import numpy as np
import scipy as st
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = {
    "Country":['India','Pakistan','Bhutan','Bangladesh','Nepal','Sri lanka','Burma','China','Afghanistan'],
    "Age":[49,32,35,43,45,40,np.nan,53,55],
    "Salary":[62000,38000,44000,51000,np.nan,48000,42000,69000,73000],
    "Purchase":['No','Yes','No','No','Yes','Yes','No','Yes','No']
}

df = pd.DataFrame(data)
print(data)

#calculate missing values
print(df.isnull().sum())
print("\nTotal missing values :",df.isnull().sum().sum())

#clean and preprocess the dataset remove the missing values
df_droped = df.dropna()
print(df_droped)

#mean
df_mean = df.copy()
df_mean["Age"] = df_mean['Age'].fillna(df_mean['Age'].mean())

df_mean['Salary'] = df_mean['Salary'].fillna(df_mean['Salary'].mean())
print(df_mean)

#median
df_median = df.copy()
df_median["Age"] = df_median['Age'].fillna(df_median['Age'].median())

df_median['Salary'] = df_median['Salary'].fillna(df_median['Salary'].median())
print(df_median)

#mode
df_mode = df.copy()
df_mode["Age"] = df_mode['Age'].fillna(df_mode['Age'].mode()[0])
df_mode['Salary'] = df_mode['Salary'].fillna(df_mode['Salary'].mode()[0])
print(df_mode)

#Encode categorical data
df_encoded = df_mean.copy()

le = LabelEncoder()
df_encoded['Purchase'] = le.fit_transform(df_encoded['Purchase'])
le = LabelEncoder()
df_encoded['Country'] = le.fit_transform(df_encoded['Country'])
print(df_encoded)


#linear regression model
X = df_encoded[['Age','Salary']]
y = df_encoded['Purchase']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.33,random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test,y_pred)
print(accuracy*100,"%")



plt.scatter(y_test,y_pred)
plt.title("Scatter graph")
plt.xlabel("actual_values")
plt.ylabel("predicted_values")
plt.show()

