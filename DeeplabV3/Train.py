# -*- coding: utf-8 -*-
"""
@File    : Train.py
@Time    : 2019/8/23 10:18
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import matplotlib.pyplot as plt
import torch.optim as optim
from torchvision import transforms
from torchvision.datasets.voc import VOCSegmentation

from own.model.DeeplabV3 import *


def Train(model, train_loader, criterion, optimizer, device, metrics=None, lr_scheduler=None, epoch=30):
    """

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
        # show_data(image, label)
        image, label = image.to(device), label.to(device)
        optimizer.zero_grad()
        output = model(image)
        # VOC 2007 输入图片为PNG格式 ，单通道
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
                         loss.item()))


def Test(model, test_loader, criterion, device):
    """

    :param model: 模型
    :param test_loader: 测试集
    :param criterion: 损失
    :param device: GPU 或者CPU
    :return:
    """
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for image, label in test_loader:
            image, label = image.to(device), label.to(device)
            output = model(image)
            loss = criterion(output, label.long().unsqueeze(0))
            test_loss += loss.item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(label.view_as(pred)).sum().item()

    test_loss /= len(test_loss.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


def show_data(image, label):
    plt.subplot(121)
    a = image[1, :, :, :]
    plt.imshow(a.permute(1, 2, 0))
    plt.subplot(122)
    b = label[1, 1, :, :]
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

    torch.cuda.set_device(3)
    device = torch.device("cuda")
    model = Deeplab().to(device)
    loss = nn.CrossEntropyLoss().to(device)
    optimizer = optim.SGD(model.parameters(), lr=0.0001, momentum=0.8)

    for epoch in range(30):
        Train(model, train_loader=train_loader,
              criterion=loss, optimizer=optimizer,
              device=device, epoch=epoch)


if __name__ == '__main__':
    main()
