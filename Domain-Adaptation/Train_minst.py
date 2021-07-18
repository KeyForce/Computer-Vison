# -*- coding: utf-8 -*-
"""
@File    : Train_minst.py
@Time    : 2020/1/4 16:01
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import keras
import matplotlib.pyplot as plt
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD
from sklearn import manifold

f = np.load('./mnist.npz')
x_train, y_train, x_test, y_test = f['x_train'], f['y_train'], f['x_test'], f['y_test']

print(x_train.shape)  # (60000, 28, 28)
print(x_test.shape)  # (10000, 28, 28)
# img = plt.imshow(x_train[0],cmap='gray')
# plt.show()


x_train = x_train.reshape(60000, 784)  # 将图片摊平，变成向量
x_test = x_test.reshape(10000, 784)

x_train = x_train / 255
x_test = x_test / 255

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(256, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()
model.compile(optimizer=SGD(), loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, batch_size=64, epochs=5, validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
model.save('./minst.h5')

# 绘制训练 & 验证的准确率值
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()


