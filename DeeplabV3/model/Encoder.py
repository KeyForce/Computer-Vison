# -*- coding: utf-8 -*-
"""
@File    : Encoder.py
@Time    : 2019/8/22 11:05
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import torch
import torch.nn as nn
import torch.nn.functional as F


class ASSP_Module(nn.Module):
    def __init__(self, in_chanels, out_channels, kernel_size, padding, dilation):
        super(ASSP_Module, self).__init__()

        self.atrous_conv = nn.Conv2d(in_chanels, out_channels, kernel_size,
                                     stride=1, padding=padding, dilation=dilation, bias=False)

        # self.bn = nn.SyncBatchNorm(out_channels)
        self.bn = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU()
        self.init_weight()

    def init_weight(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                torch.nn.init.kaiming_normal_(m.weight)
            elif isinstance(m, nn.SyncBatchNorm):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()

    def forward(self, x):
        x = self.atrous_conv(x)
        x = self.bn(x)
        x = self.relu(x)

        return x


class ASSP(nn.Module):
    def __init__(self):
        super(ASSP, self).__init__()

        # 使用MobileNet作为主干网络 in_channel = 320
        in_channel = 320

        # 过程按照论文原文
        self.assp1 = ASSP_Module(in_channel, out_channels=256, kernel_size=1, padding=0, dilation=1)
        self.assp2 = ASSP_Module(in_channel, out_channels=256, kernel_size=3, padding=6, dilation=6)
        self.assp3 = ASSP_Module(in_channel, out_channels=256, kernel_size=3, padding=12, dilation=12)
        self.assp4 = ASSP_Module(in_channel, out_channels=256, kernel_size=3, padding=18, dilation=18)
        self.image_pool = nn.Sequential(nn.AdaptiveAvgPool2d((1, 1)),
                                        nn.Conv2d(in_channel, out_channels=256, kernel_size=1, bias=False),
                                        # nn.SyncBatchNorm(256),
                                        nn.BatchNorm2d(256),
                                        nn.ReLU()
                                        )

        self.conv1 = nn.Sequential(nn.Conv2d(1280, 256, kernel_size=1, bias=False),
                                   nn.BatchNorm2d(256),
                                   nn.ReLU(),
                                   nn.Dropout(0.5)
                                   )

    def forward(self, x):
        x1 = self.assp1(x)
        x2 = self.assp2(x)
        x3 = self.assp3(x)
        x4 = self.assp4(x)
        x5 = self.image_pool(x)
        x5 = F.interpolate(x5, size=x4.size()[2:], mode='bilinear', align_corners=True)
        x = torch.cat((x1, x2, x3, x4, x5), dim=1)
        x = self.conv1(x)

        return x


if __name__ == '__main__':
    import time
    from torch.autograd import Variable

    image_width = 480
    image_height = 480
    model = ASSP()
    print(model)

    x = Variable(torch.rand(2, 320, image_height, image_width))
    start = time.time()
    x, x1, x2, x3, x4, x5 = model(x)
    end = time.time()
    print(x.shape)
    # print('{0} {1} {2} {3} {4} {5}'.format(x.shape, x1.shape, x2.shape, x3.shape, x4.shape, x5.shape))
    print(end - start)
