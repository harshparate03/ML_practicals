# from sklearn.datasets import load_iris

# iris = load_iris()
# x = iris.data
# y = iris.target
# feature_names = iris.feature_names
# target_names = iris.target_names
# print("Feature names: ",feature_names)
# print("Target names: ",target_names)
# print("First 5 rows : ",x[:5])


from sklearn.preprocessing import LabelEncoder
categorical_feature = ['cat','dog','cat','dog','bird']
encoder = LabelEncoder()
encoded_feature = encoder.fit_transform(categorical_feature)
print(categorical_feature)