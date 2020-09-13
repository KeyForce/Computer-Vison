# Computer-Vison

### 项目

* Dynamic U-Net-Segment 

  * ResNet34 + Unet 在小的数据集上效果不错。
  * 小的数据集选择参数量小的网络，减小通道数与层数，减弱正则化，迭代次数不能太大。网络太硬影响收敛速度，网络软一点效果好。
  * Adam采用自适应学习率模型收敛较快，但最终模型变现不如SGD。
  
  ![1569054114772](image/1569054114772.png)
  
* DeeplabV3+

  ![1569054180948](image/1569054180948.png)

* Classification

  ![Figure](image/Figure.png)

* YOLO V4

* [AIOT](https://github.com/KeyForce/Computer-Vison/tree/master/AIOT/DEMO1)

  * 网页端实现开灯关灯

<div align=center><img src ="image/AIOT.png"/></div>



* Domain-Adaptation

  <div align=center><img src ="image/image-20200524152211570-1597029532519.png"width="550"/></div>

* 7-Segment-Digital-Recongnition

  步骤1：提取仪表LCD显示屏。高斯滤波、Canny边缘检测、四点透视变换。

  步骤2：提取数字区域。阈值处理、形态学操作、ROI提取。

  步骤3：识别数字。SVM分类。

  <div align=center><img src ="image/微信截图_20190517223708.png"/></div>

### 其他

* [NoteBook](https://github.com/KeyForce/NoteBook)
* Leetcode

