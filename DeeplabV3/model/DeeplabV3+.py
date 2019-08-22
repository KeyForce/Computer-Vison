# -*- coding: utf-8 -*-
"""
@File    : DeeplabV3+.py
@Time    : 2019/8/22 16:36
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from MobilenetV2 import *
from Encoder import *
from Decoder import *



class Deeplab(nn.Module):
    def __init__(self):
        super(Deeplab, self).__init__()

        self.backbone = MobileNetV2()
        self.encoder = ASSP()
        self.decoder = Decoder()

    def forward(self, input):
        x, low_lever_feature = self.backbone(input)
        x = self.encoder(x)
        x = self.decoder(x, low_lever_feature)
        x = F.interpolate(x, size=input.size()[2:], mode='bilinear', align_corners=True)

        return x

if __name__ == '__main__':
    import time
    from torch.autograd import Variable

    image_width = 480
    image_height = 480
    model = Deeplab()
    print(model)

    x = Variable(torch.rand(2, 3, image_height, image_width))
    start = time.time()
    x = model(x)
    end = time.time()
    print(x.shape)
    # print('{0} {1} {2} {3} {4} {5}'.format(x.shape, x1.shape, x2.shape, x3.shape, x4.shape, x5.shape))
    print(end - start)
