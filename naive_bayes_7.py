import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

data = {
    "Outlook":['Sunny','Sunny','Overcast','Rain','Rain','Overcast','Sunny','Sunny','Overcast','Rain'],
    "Temperature":[ 'Hot', 'Hot', 'Hot', 'Mild', 'Mild','Hot', 'Hot', 'Hot', 'Hot', 'Mild'],
    "Humidity":[ 'High', 'High', 'High', 'High', 'Low','High', 'Low', 'High', 'High', 'High'],
    "Wind":[ 'Weak', 'Strong', 'Weak', 'Weak', 'Strong','Strong', 'Weak', 'Weak', 'Strong', 'Strong'],
    "Play_Tennis":['No', 'No', 'Yes', 'Yes', 'No','No', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)
print(df)

X = df[['Outlook','Temperature','Humidity','Wind']]
y = df['Play_Tennis']

le_outlook = LabelEncoder()
X['Outlook'] = le_outlook.fit_transform(X['Outlook'])

le_Temperature = LabelEncoder()
X['Temperature'] = le_Temperature.fit_transform(X['Temperature'])

le_Humidity = LabelEncoder()
X['Humidity'] = le_Humidity.fit_transform(X['Humidity'])

le_Wind = LabelEncoder()
X['Wind'] = le_Wind.fit_transform(X['Wind'])

print("\n Now the train data is: ")

le_Play_Tennis = LabelEncoder()
y = le_Play_Tennis.fit_transform(y)

print("\nNow the Train output is:\n", y)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
gb = GaussianNB()
gb.fit(X_train,y_train)

y_pred = gb.predict(X_test)

print("Accuracy:",accuracy_score(y_test,y_pred)*100,"%")


pred = gb.predict([[2,0,0,1]])
print(pred)
print(y_test,gb.predict(X_test))