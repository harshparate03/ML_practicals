import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import CategoricalNB


data = {
    "Item_no":[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    "Age":['Youth','Youth','Middle','Senior','Senior','Middle','Senior','Youth','Youth','Senior','Youth','Middle','Middle','Senior'],
    "Income":['High','High','High','Medium','Low','Low','Low','Medium','Low','High','Medium','Medium','High','Medium'],
    "Students":['No','No','No','No','Yes','Yes','Yes','No','Yes','Yes','Yes','No','Yes','Yes'],
    "Credits":['Fair','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Excellent'],
    "Buy_Computers":['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

X = df[['Item_no','Age','Income','Students','Credits']]
y = df['Buy_Computers']

encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X).astype(int)
print(X_encoded)

model = CategoricalNB()
model.fit(X_encoded,y)

test_data = pd.DataFrame(
    [["15","Youth","Low","No","Fair"]],
)
test_encoded = encoder.fit_transform(test_data).astype(int)
print(test_encoded)

pred = model.predict(test_encoded)
print("prediction : ", pred[0])
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import CategoricalNB


data = {
    "Item_no":[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    "Age":['Youth','Youth','Middle','Senior','Senior','Middle','Senior','Youth','Youth','Senior','Youth','Middle','Middle','Senior'],
    "Income":['High','High','High','Medium','Low','Low','Low','Medium','Low','High','Medium','Medium','High','Medium'],
    "Students":['No','No','No','No','Yes','Yes','Yes','No','Yes','Yes','Yes','No','Yes','Yes'],
    "Credits":['Fair','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Excellent'],
    "Buy_Computers":['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

X = df[['Item_no','Age','Income','Students','Credits']]
y = df['Buy_Computers']

encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X).astype(int)
print(X_encoded)

model = CategoricalNB()
model.fit(X_encoded,y)

test_data = pd.DataFrame(
    [["Youth","Low","No","Fair"]],
)
test_encoded = encoder.fit_transform(test_data).astype(int)
print(test_encoded)

pred = model.predict(test_encoded)
print("prediction : ", pred[0])
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import CategoricalNB


data = {
    "Item_no":[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    "Age":['Youth','Youth','Middle','Senior','Senior','Middle','Senior','Youth','Youth','Senior','Youth','Middle','Middle','Senior'],
    "Income":['High','High','High','Medium','Low','Low','Low','Medium','Low','High','Medium','Medium','High','Medium'],
    "Students":['No','No','No','No','Yes','Yes','Yes','No','Yes','Yes','Yes','No','Yes','Yes'],
    "Credits":['Fair','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Excellent'],
    "Buy_Computers":['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

X = df[['Item_no','Age','Income','Students','Credits']]
y = df['Buy_Computers']

encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X).astype(int)
print(X_encoded)

model = CategoricalNB()
model.fit(X_encoded,y)

test_data = pd.DataFrame(
    [["Youth","Low","No","Fair"]],
)
test_encoded = encoder.fit_transform(test_data).astype(int)
print(test_encoded)

pred = model.predict(test_encoded)
print("prediction : ", pred[0])
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import CategoricalNB


data = {
    "Item_no":[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    "Age":['Youth','Youth','Middle','Senior','Senior','Middle','Senior','Youth','Youth','Senior','Youth','Middle','Middle','Senior'],
    "Income":['High','High','High','Medium','Low','Low','Low','Medium','Low','High','Medium','Medium','High','Medium'],
    "Students":['No','No','No','No','Yes','Yes','Yes','No','Yes','Yes','Yes','No','Yes','Yes'],
    "Credits":['Fair','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Excellent'],
    "Buy_Computers":['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

X = df[['Item_no','Age','Income','Students','Credits']]
y = df['Buy_Computers']

encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X).astype(int)
print(X_encoded)

model = CategoricalNB()
model.fit(X_encoded,y)

test_data = pd.DataFrame(
    [["Youth","Low","No","Fair"]],
)
test_encoded = encoder.fit_transform(test_data).astype(int)
print(test_encoded)

pred = model.predict(test_encoded)
print("prediction : ", pred[0])
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import CategoricalNB


data = {
    "Item_no":[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    "Age":['Youth','Youth','Middle','Senior','Senior','Middle','Senior','Youth','Youth','Senior','Youth','Middle','Middle','Senior'],
    "Income":['High','High','High','Medium','Low','Low','Low','Medium','Low','High','Medium','Medium','High','Medium'],
    "Students":['No','No','No','No','Yes','Yes','Yes','No','Yes','Yes','Yes','No','Yes','Yes'],
    "Credits":['Fair','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Excellent'],
    "Buy_Computers":['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

X = df[['Item_no','Age','Income','Students','Credits']]
y = df['Buy_Computers']

encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X).astype(int)
print(X_encoded)

model = CategoricalNB()
model.fit(X_encoded,y)

test_data = pd.DataFrame(
    [["Youth","Low","No","Fair"]],
)
test_encoded = encoder.fit_transform(test_data).astype(int)
print(test_encoded)

pred = model.predict(test_encoded)
print("prediction : ", pred[0])
