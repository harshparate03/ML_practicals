import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay,precision_score,recall_score,f1_score
import matplotlib.pyplot as plt

data = {
    'Country': ['France','Spain','Germany','France','Spain','Germany','Spain','France','Spain'],
    'Age': [44.00,44.00,54.00,34.00,44.00,34.00,23.00,45.00,23.00],
    'Salary': [44000.0,50000.0,24000.0,np.nan,np.nan,23667.0,67000.0,45000.0,56000.0],
    'Purchased': ['Yes','No','Yes','Yes','No','Yes','Yes','No','No']
}

df = pd.DataFrame(data)
print(df)

#mising values
print("=========missing values===========")
print(df.isnull().sum())
print("=========================")

#categorical values
print("=========categorical values===========")

df_encoded = df.copy()

le = LabelEncoder()
df_encoded['Country'] = le.fit_transform(df_encoded['Country'])

le =  LabelEncoder()
df_encoded['Purchased'] = le.fit_transform(df_encoded['Purchased'])

print(df_encoded)

print("==========================")
print("============Splitting dataset into Trainning and test dataset==============")

X = df_encoded[['Country','Age','Salary']]
y = df_encoded['Purchased']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)

#fill the missing values
mean_salary = X['Salary'].mean()

X_train = X_train.fillna({'Salary' :mean_salary})
X_test = X_test.fillna({'Salary': mean_salary})
print("======Missing values=========")
print("Train ")
print(X_train)
print("Test ")
print(X_test)


#feature scalling
Scaler = StandardScaler()

X_train_scaled = Scaler.fit_transform(X_train)
X_train_scaled = Scaler.transform(X_test)

print(X_train_scaled)
print(X_train_scaled)


#logistic regression
model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test,y_pred)
print(accuracy)

#confusion matrix
com = confusion_matrix(y_test,y_pred)
cm_display = ConfusionMatrixDisplay(confusion_matrix=com,display_labels=[0,1])
cm_display.plot()
plt.show()

#precision
precision = precision_score(y_test,y_pred)
print("Precision : ", precision)

#Sensitivity
sensitivity = recall_score(y_pred,y_test)
print(sensitivity)

#f1_score
f1_score = f1_score(y_pred,y_test)
print("F1 score",f1_score)