# -*- coding: utf-8 -*-
"""
@File    : Decoder.py
@Time    : 2019/8/22 15:57
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import torch
import torch.nn as nn
import torch.nn.functional as F


class Decoder(nn.Module):
    def __init__(self, num_classes=2):
        super(Decoder, self).__init__()
        #  Mobilenet
        in_channel = 24

        self.conv1 = nn.Sequential(nn.Conv2d(in_channels=in_channel, out_channels=48, kernel_size=1, bias=False),
                                   nn.BatchNorm2d(48),
                                   nn.ReLU()
                                   )
        # 这边与论文不太相同
        self.conv2 = nn.Sequential(nn.Conv2d(in_channels=304, out_channels=256, kernel_size=3, padding=1, bias=False),
                                   nn.BatchNorm2d(256),
                                   nn.ReLU(),
                                   nn.Dropout(0.5),
                                   nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1, bias=False),
                                   nn.BatchNorm2d(256),
                                   nn.ReLU(),
                                   nn.Dropout(0.1),
                                   nn.Conv2d(256, num_classes, kernel_size=1, stride=1)
                                   )
        self.init_weight()

    def forward(self, x, low_level_feat):
        low_level_feat = self.conv1(low_level_feat)

        x = F.interpolate(x, size=low_level_feat.size()[2:], mode='bilinear', align_corners=True)
        x = torch.cat((x, low_level_feat), dim=1)
        x = self.conv2(x)

        return x

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

