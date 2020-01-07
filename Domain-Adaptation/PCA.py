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
import numpy as np
from matplotlib import cm

mnist = datasets.load_digits()
X = mnist.data
Y = mnist.target
pca = decomposition.PCA(n_components=3)
Data = pca.fit_transform(X)

num_class = [i for i in range(9)]
fig = plt.figure()
ax = Axes3D(fig)
#列表解析
num0 = np.array([Data[i] for i,v in enumerate(Y) if v == 0])
# 动态创建变量number 0~9
# names = locals()
# for i in range(9):
#     names['number' + str(i)] = np.array([Data[index] for index,v in enumerate(Y) if v == i])
for i in range(10):
    number = np.array([Data[index] for index, v in enumerate(Y) if v == i])


    for x, y, z in zip(number[:, 0], number[:, 1], number[:, 2]):
        print(x,y,z)
        c = cm.rainbow(int(255 * i / 9))  # 上色
        ax.text(x, y, z, str(i), backgroundcolor=c)  # 标位子
    # ax.scatter(number[:, 0], number[:, 1], number[:, 2], label='Number-' + str(i))

# ax.scatter(num0[:, 0], num0[:, 1], num0[:, 2], c=0,label='Number 0')
# ax.scatter(new_X[:, 0], new_X[:, 1], new_X[:, 2], c=Y, label='Number')
# 坐标轴
ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_zlim(-30, 30)
# plt.legend(loc=2)
plt.show()
