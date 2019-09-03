# -*- coding: utf-8 -*-
"""
@File    : utils.py
@Time    : 2019/9/2 9:06
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import numpy as np

# def get_pascal_labels():
#     """加载不同标签的RGB值
#     Returns:
#         np.ndarray with dimensions (21, 3)
#     """
#     label_colours = [(0, 0, 0),  # 0=background
#                      # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
#                      (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
#                      # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
#                      (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0),
#                      # 11=dining table, 12=dog, 13=horse, 14=motorbike, 15=person
#                      (192, 128, 0), (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128),
#                      # 16=potted plant, 17=sheep, 18=sofa, 19=train, 20=tv/monitor
#                      (0, 64, 0), (128, 64, 0), (0, 192, 0), (128, 192, 0), (0, 64, 128)]
#
#     return np.asarray(label_colours)


def get_pascal_labels():
    """Load the mapping that associates pascal classes with label colors
    Returns:
        np.ndarray with dimensions (21, 3)
    """
    return np.asarray([[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0],
                       [0, 0, 128], [128, 0, 128], [0, 128, 128], [128, 128, 128],
                       [64, 0, 0], [192, 0, 0], [64, 128, 0], [192, 128, 0],
                       [64, 0, 128], [192, 0, 128], [64, 128, 128], [192, 128, 128],
                       [0, 64, 0], [128, 64, 0], [0, 192, 0], [128, 192, 0],
                       [0, 64, 128]])


def decode_segmap(label_mask):
    """将模型输出的标签转换为彩色图
    Args:
        label_mask (np.ndarray): an (M,N) array of integer values denoting
          the class label at each spatial location.
    Returns:
        (np.ndarray, optional): the resulting decoded color image.
    """
    n_classes = 21
    label_colours = get_pascal_labels()

    r = label_mask.copy()
    g = label_mask.copy()
    b = label_mask.copy()
    for ll in range(0, n_classes):
        r[label_mask == ll] = label_colours[ll, 0]
        g[label_mask == ll] = label_colours[ll, 1]
        b[label_mask == ll] = label_colours[ll, 2]
    rgb = np.zeros((label_mask.shape[0], label_mask.shape[1], 3))
    rgb[:, :, 0] = r / 255.0
    rgb[:, :, 1] = g / 255.0
    rgb[:, :, 2] = b / 255.0

    return rgb
