# -*- coding: utf-8 -*-
"""
@File    : Train.py
@Time    : 2019/8/23 10:18
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import matplotlib.pyplot as plt
import numpy as np
import torch.optim as optim
from torchvision import transforms
from torchvision.datasets.voc import VOCSegmentation

from own.model.DeeplabV3 import *


def Train(model, train_loader, criterion, optimizer, device, metrics=None, lr_scheduler=None, epoch=30):
    """
    训练模型
    :param model: 模型
    :param train_loader: 训练集
    :param criterion: 损失
    :param optimizer: 优化器
    :param device: GPU 或者CPU
    :param metrics: 评价指标
    :param lr_scheduler: 学习率调整
    :param epoch: 迭代次数
    :return:
    """
    model.train()
    for batch_idx, (image, label) in enumerate(train_loader):
        # show_train_data(image, label)
        image, label = image.to(device), label.to(device)
        optimizer.zero_grad()
        output = model(image)
        # VOC 2007 输入图片为PNG格式 ，单通道，输入label为（Batch，1, H，W）格式 需要转换成（Batch，H，W）
        label = label.long().squeeze(1)
        loss = criterion(output, label)
        loss.backward()
        optimizer.step()
        # Log
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.
                  format(epoch,
                         batch_idx * len(image),
                         len(train_loader.dataset),
                         100. * batch_idx / len(train_loader),
                         loss.item())
                  )


def Test(model, test_loader, criterion, device):
    """
    测试模型
    :param model: 模型
    :param test_loader: 测试集
    :param criterion: 损失
    :param device: GPU 或者CPU
    :return:
    """
    model.eval()
    test_loss = 0
    correct = 0
    confusion_matrix = np.zeros((20, 20))
    with torch.no_grad():
        for image, label in test_loader:
            image, label = image.to(device), label.to(device)
            output = model(image)
            label = label.long().squeeze(1)
            loss = criterion(output, label)
            test_loss += loss.item()
            # 获取最大对数概率的索引 output channel 20个中找个最大的
            pred = output.argmax(dim=1, keepdim=True)

            # PA像素精度
            num_class = 20
            pre_image = pred.squeeze(1).cpu().numpy()
            plt.imshow(pre_image[0,:,:])
            plt.show()
            gt_image = label.cpu().numpy()

            confusion_matrix += fast_hist(gt_image, pre_image, num_class)

    correct = np.diag(confusion_matrix).sum() / confusion_matrix.sum()
    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}\n'.
          format(loss,
                 correct,
                 )
          )


def fast_hist(a, b, n):
    k = (a >= 0) & (a < n)
    return np.bincount(n * a[k].astype(int) + b[k], minlength=n**2).reshape(n, n)

def show_train_data(image, label):
    """
    展示经过transform之后的图片与标签
    :param image:
    :param label:
    :return:
    """
    plt.subplot(121)
    a = image[1, :, :, :]
    plt.imshow(a.permute(1, 2, 0))
    plt.subplot(122)
    # PNG图片只需要（H，W）
    b = label[1, 0, :, :]
    plt.imshow(b)
    plt.show()
    plt.pause(0.1)
    plt.close()


def main():
    transform = transforms.Compose([transforms.CenterCrop(500),
                                    transforms.ToTensor()])

    train_data = VOCSegmentation(root='/home/hanwei-1/',
                                 year='2007',
                                 image_set='train',
                                 transform=transform,
                                 target_transform=transform,
                                 download=False)
    test_data = VOCSegmentation(root='/home/hanwei-1/',
                                year='2007',
                                image_set='val',
                                transform=transform,
                                target_transform=transform,
                                download=False)

    # 使用drop_last让Batch能够整除
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=2, drop_last=True)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=2, drop_last=True)

    # 设置GPU
    torch.cuda.set_device(1)
    device = torch.device("cuda")
    # 初始化模型，损失，优化器
    model = Deeplab().to(device)
    loss = nn.CrossEntropyLoss().to(device)
    optimizer = optim.SGD(model.parameters(), lr=0.0001, momentum=0.8)
    # 开始训练
    confusion_matrix = np.zeros((20, 20))
    for epoch in range(30):
        Train(model, train_loader=train_loader,
              criterion=loss, optimizer=optimizer,
              device=device, epoch=epoch)
        Test(model, test_loader, loss, device)


if __name__ == '__main__':
    main()
