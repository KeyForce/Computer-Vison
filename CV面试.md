### 1.介绍Faster RCNN的流程及损失函数，为什么这样设计损失函数

![img](image/v2-c0172be282021a1029f7b72b51079ffe_hd.jpg)

![img](image/20170324121024882)

* 先通过主干网络（Backbone）提取特征图

* 在通过RPN网络判断anchors属于前景还是背景，这里RPN网络包括两个部分，Anchor的生成和两层的卷积层