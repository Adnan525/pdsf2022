import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

# we can use while true: and put the program in a loop if we need to ask the user repeatedly
# for now, the program will terminate after 1 plot
print("input 2 numbers from between 0 to 3.")
try:
    a = int(input("a: "))
    b = int(input("b: "))
    # raise an exception ValueError if any of the numbers are smaller than 0 or bigger than 5
    # the next catch block will catch the error, print message and continue
    if a < 0 or a > 3 or b < 0 or b > 3:
        raise ValueError
except ValueError:
    print("input error, must be between 0 and 3 (inclusive)")

iris = datasets.load_iris()  # returns np-array (150 rows and 4 columns)

# Each row is a 4D sample
# Column: Sepal Length, Sepal Width, Petal Length and Petal Width.
X = iris.data[:, [a, b]]  # take the first two columns.
y = iris.target
# Target names: Setosa, Versicolour, and Virginica
# labels = iris.target_names
# Plot the data
plt.scatter(X[:, 0], X[:, 1], label='iris', c='r', marker='o', s=30)
plt.xlabel(iris['feature_names'][a])
plt.ylabel(iris['feature_names'][b])
plt.title('iris dataset')
plt.legend()
plt.show()
