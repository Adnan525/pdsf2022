import numpy
from sklearn import datasets, neighbors, metrics, svm
from sklearn.model_selection import train_test_split
import pandas as pd

# following Kaggle template
dataset = datasets.load_iris()
# get the dataset
X = dataset.data
# shape of the dataset
n_samples, n_features = X.shape
# predict variable
y = dataset.target
# prediction choices
# since we have 3 choices, we will have 3x3 confusion matrix
class_names = dataset.target_names
print(class_names)
# dividing dataset by train : test = 0.75 : 0.25
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
# Load classifier containing classification technique and model
# using knn
knn = neighbors.KNeighborsClassifier(n_neighbors=3)
# Training
knn.fit(X_train, y_train)
# Testing
y_pred = knn.predict(X_test)


# function to generate the confusion matrix
def get_confusion_matrix(true_list, predicted_list, class_labels):
    c_matrix = pd.crosstab(predicted_list, true_list)
    c_matrix = c_matrix.set_axis(class_labels, axis=0, inplace=False)
    c_matrix = c_matrix.set_axis(class_labels, axis=1, inplace=False)
    return c_matrix


labels = ['Setosa', 'Versicolour', 'Virginica']
confusion_matrix = get_confusion_matrix(y_test, y_pred, labels)
print(confusion_matrix)
