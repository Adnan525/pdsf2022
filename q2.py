from sklearn import datasets


def load_iris_dataset():
    # scikit will load the data using datasets
    # the loaded dataset is a bunch which is just a subclass of dictionary
    # key/attribute values are data, target, frame, target_names, DESCR etc.
    # we will just return data, target and target_names

    df = datasets.load_iris()
    # for item in df:
    #     print(item)
    return df["data"], df["target"], df["target_names"]


X, y, class_labels = load_iris_dataset()
print('X =', X)
print('y =', y)
print('class labels =', class_labels)
