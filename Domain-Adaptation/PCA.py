# -*- coding: utf-8 -*-
"""
@File    : PCA.py
@Time    : 2020/1/5 15:10
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn import decomposition

mnist = datasets.load_digits()
X = mnist.data
Y = mnist.target
pca = decomposition.PCA(n_components=3)
new_X = pca.fit_transform(X)

num_class = [i for i in range(9)]
fig = plt.figure()
ax = Axes3D(fig)
for i in range(1797):
    x, y, z = new_X[i,0],new_X[i,1],new_X[i,2]
    color = Y[i]
    ax.scatter(x, y, z, c=color, label=color)

# ax.scatter(new_X[:, 0], new_X[:, 1], new_X[:, 2], c=y, label=num_class)
plt.legend(loc=2)
plt.show()
