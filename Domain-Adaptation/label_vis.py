# -*- coding: utf-8 -*-
"""
@File    : label_vis.py
@Time    : 2021/3/31 12:35
@Author  : KeyForce
@Email   : july.master@outlook.com
"""
import os.path
import xml.etree.ElementTree as xmlET

import numpy as np
from PIL import Image, ImageDraw
from PIL import ImageFont

classes = ('__background__',  # always index 0
           'Broken gate', 'Scratch', 'Pollution', 'Dark', 'crack')

file_path_img = '/home/wild/ELVOC2007/CRACK2/CRACKJPG'
file_path_xml = '/home/wild/ELVOC2007/CRACK2/CRACKXML'
save_file_path = '/home/wild/ELVOC2007/CRACK2/CRACKVIS'


def plot_one_box_PIL(box, img, color=None, fontcolor=None, label=None, line_thickness=None):
    #     img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    line_thickness = line_thickness or max(int(min(img.size) / 200), 2)
    draw.rectangle(box, width=line_thickness, outline=tuple(color))  # plot
    if label:
        fontsize = fontsize = max(round(max(img.size) / 60), 12)
        font = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", fontsize)
        txt_width, txt_height = font.getsize(label)
        if (box[1] - txt_height) < 0:
            draw.rectangle([box[0], box[1] + txt_height + 2, box[0] + txt_width + 2, box[1]], fill=tuple(color))
            draw.text((box[0], box[1]), label, fill=fontcolor, font=font)
        else:
            draw.rectangle([box[0], box[1] - txt_height + 4, box[0] + txt_width, box[1]], fill=tuple(color))
            draw.text((box[0], box[1] - txt_height), label, fill=fontcolor, font=font)
    return np.asarray(img)


pathDir = os.listdir(file_path_xml)

for idx in range(len(pathDir)):
    filename = pathDir[idx]
    tree = xmlET.parse(os.path.join(file_path_xml, filename))
    objs = tree.findall('object')
    num_objs = len(objs)
    boxes = np.zeros((num_objs, 5), dtype=np.uint16)

    for ix, obj in enumerate(objs):
        bbox = obj.find('bndbox')
        # Make pixel indexes 0-based
        x1 = float(bbox.find('xmin').text) - 1
        y1 = float(bbox.find('ymin').text) - 1
        x2 = float(bbox.find('xmax').text) - 1
        y2 = float(bbox.find('ymax').text) - 1

        cla = obj.find('name').text
        label = classes.index(cla)

        boxes[ix, 0:4] = [x1, y1, x2, y2]
        boxes[ix, 4] = label

    image_name = os.path.splitext(filename)[0]
    img = Image.open(os.path.join(file_path_img, image_name + '.jpg'))
    print(image_name)
    img = img.convert("RGB")

    for ix in range(len(boxes)):
        xmin = int(boxes[ix, 0])
        ymin = int(boxes[ix, 1])
        xmax = int(boxes[ix, 2])
        ymax = int(boxes[ix, 3])
        label = classes[boxes[ix, 4]]
        if label == 'Broken gate':
            label = "断栅"
            color = (255, 255, 0)
            fontcolor = (0, 0, 0)
        if label == 'Scratch':
            label = "划痕"
            color = (0, 0, 255)
            fontcolor = (255, 255, 255)
        if label == 'Pollution':
            label = "黑斑"
            color = (0, 255, 255)
            fontcolor = (0, 0, 0)
        if label == 'Dark':
            label = "黑斑"
            color = (0, 255, 255)
            fontcolor = (0, 0, 0)

        if label == 'crack':
            label = "破裂"
            color = (255,128,0)
            fontcolor = (0, 0, 0)

        plot_one_box_PIL([xmin, ymin, xmax, ymax], img, label=label, color=color, fontcolor=fontcolor, line_thickness=3)

    img.save(os.path.join(save_file_path, image_name + '.png'))
