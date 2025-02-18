import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# url = 'iris.data'

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

irisdata = pd.read_csv(url, names=names)
# print(irisdata)

# Assign data from first four columns to X variable
X = irisdata.iloc[:, 0:4]

# Assign data from first fifth columns to y variable
y = irisdata.select_dtypes(include=[object])


# print(X)
# print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
print ('The machine is learning...')
mlp.fit(X_train, y_train.values.ravel())

print ('Predicting...')
predictions = mlp.predict(X_test)
# count = 1 
# for line in mlp.predict(X_train):
#   print (count, line )
#   count += 1

print ('Calculating Accuracy...')
count = 1
mlp_score = mlp.score(X_train, y_train)
print (mlp_score)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))


