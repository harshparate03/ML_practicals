# import pandas as pd
# from sklearn.model_selection import train_test_split 
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score

# data = {
#     'Height':[158,158,158,160,160,163,163,160,163,165,165,165,168,168,168,170,170,170],
#     'Weight':[58,59,63,59,60,60,61,64,64,61,62,65,62,63,66,63,64,68],
#     'Size':['M','M','M','M','M','M','M','L','L','L','L','L','L','L','L','L','L','L']
# }
# df = pd.DataFrame(data)

# X = df[['Height','Weight']]
# y = df['Size']

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42,stratify=y)

# Scaler = StandardScaler()

# X_train = Scaler.fit_transform(X_train)
# X_test = Scaler.transform(X_test)

# k = 2
# model = KNeighborsClassifier(n_neighbors=k)

# model.fit(X_train,y_train)


# y_pred = model.predict(X_test)

# accuracy = accuracy_score(y_test,y_pred)
# print("Accuracy : ",accuracy*100,'%')

# height = float(input("Enter the height :"))
# weight = float(input("Enter the weight : "))
# customer = Scaler.transform([[height,weight]])

# prediction = model.predict(customer)
# print("Predicted T-Shirt size : ",prediction[0])






import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
data = {
    'Height':[158,158,158,160,160,163,163,160,163,165,165,165,168,168,168,170,170,170],
    'Weight':[58,59,63,59,60,60,61,64,64,61,62,65,62,63,66,63,64,68],
    'Size':['M','M','M','M','M','M','M','L','L','L','L','L','L','L','L','L','L','L']
}
df = pd.DataFrame(data)
X = df[['Height','Weight']]
y = df['Size']

X_train , X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42,stratify=y)

Scaler = StandardScaler()
X_train = Scaler.fit_transform(X_train)
X_test = Scaler.transform(X_test)
k=2
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy Score : ", accuracy*100,'%')

h = float(input("Enter the height :"))
w = float(input("Enter the weight :"))
customer = Scaler.transform([[h,w]])
pred = model.predict(customer)
print("Predicted Size :",pred[0])
