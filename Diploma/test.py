from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix


cancer = load_breast_cancer()
print(cancer.keys())
X = [each[:3] for each in cancer['data']]
y = cancer['target']
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
mlp = MLPClassifier(hidden_layer_sizes=(3, 4, 3))
mlp.fit(X_train, y_train)
predictions = mlp.predict(X_test)
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

print("==================NN TOPOLOGY=============")
for i in range(0, len(mlp.coefs_)):
    print("Layer " + str(i))
    print(mlp.coefs_[i])

print(mlp.intercepts_[1])





