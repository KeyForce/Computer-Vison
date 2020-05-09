import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import decomposition

data = pd.read_csv('iris.csv')
# print(data)
array1 = np.array(data)
# print(array1)
x_digits = array1[:, np.arange(1, 5, 1)]
# print(x_digits)
y_digits = array1[:, 5]

pca = decomposition.PCA(n_components=2)
X_pca = pca.fit_transform(x_digits)


# n = len(y_digits)


def plot_pca_scatter():
    colors = ['black', 'blue', 'purple']
    for i in range(len(y_digits)):
        if y_digits[i] == 'setosa':
            px = X_pca[:, 0][i]
            py = X_pca[:, 1][i]
            plt.scatter(px, py, c=colors[0])
        if y_digits[i] == 'versicolor':
            px = X_pca[:, 0][i]
            py = X_pca[:, 1][i]
            plt.scatter(px, py, c=colors[1])
        else:
            px = X_pca[:, 0][i]
            py = X_pca[:, 1][i]
            plt.scatter(px, py, c=colors[2])

    # mport matplotlib as plt

    plt.legend(np.arange(0, 3).astype(str))
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.show()


# plot_pca_scatter()
fig = plt.figure()

colors = ['black', 'blue', 'purple']
for i in range(len(y_digits)):
    if y_digits[i] == 'setosa':
        px = X_pca[:, 0][i]
        py = X_pca[:, 1][i]
        plt.scatter(px, py, c=colors[0])
    if y_digits[i] == 'versicolor':
        px = X_pca[:, 0][i]
        py = X_pca[:, 1][i]
        plt.scatter(px, py, c=colors[1])
    else:
        px = X_pca[:, 0][i]
        py = X_pca[:, 1][i]
        plt.scatter(px, py, c=colors[2])

# mport matplotlib as plt


plt.legend(np.arange(0, 3).astype(str))
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.show()
