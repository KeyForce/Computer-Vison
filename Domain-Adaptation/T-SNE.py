# -*- coding: utf-8 -*-
"""
@File    : T-SNE.py
@Time    : 2020/1/6 14:48
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn import manifold

mnist = datasets.load_digits()
X = mnist.data
Y = mnist.target

# 三维
tsne = manifold.TSNE(n_components=3, init='pca', random_state=0)
Data = tsne.fit_transform(X)

num_class = [i for i in range(9)]
fig = plt.figure()
ax = Axes3D(fig)
# 列表解析
num0 = np.array([Data[i] for i, v in enumerate(Y) if v == 0])

for i in range(10):
    number = np.array([Data[index] for index, v in enumerate(Y) if v == i])

    for x, y, z in zip(number[:, 0], number[:, 1], number[:, 2]):
        c = cm.rainbow(int(255 * i / 9))  # 上色
        ax.text(x, y, z, str(i), backgroundcolor=c)  # 标位子
    # ax.scatter(number[:, 0], number[:, 1], number[:, 2], label='Num-' + str(i))

# 坐标轴
ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_zlim(-30, 30)
ax.set_title('MNIST T-SNE 3D')
# plt.legend(loc=2)

# 二维
tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
Data = tsne.fit_transform(X)

fig = plt.figure(2)
for i in range(10):
    number = np.array([Data[index] for index, v in enumerate(Y) if v == i])
    for x, y in zip(number[:, 0], number[:, 1]):
        c = cm.rainbow(int(255 * i / 9))  # 上色
        plt.text(x, y, str(i), backgroundcolor=c)  # 标位子
    # plt.scatter(number[:, 0], number[:, 1],label='Num-' + str(i))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('MNIST T-SNE 2D')
plt.xlim(-60, 80)
plt.ylim(-80, 80)
# plt.legend()
plt.show()
