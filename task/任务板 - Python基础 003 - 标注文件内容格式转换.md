# 任务板 - Python基础 - 标注文件内容格式转换

> author：杨宁
Last modified：2020-07-22

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [任务板 - Python基础 - 标注文件内容格式转换](#任务板-python基础-标注文件内容格式转换)
	- [1. 概述](#1-概述)
	- [2. 目的](#2-目的)
	- [3. 环境要求](#3-环境要求)
	- [4. 技术要点](#4-技术要点)
	- [5. 处理方法与脚本](#5-处理方法与脚本)
	- [6. 常见问题处理](#6-常见问题处理)
	- [7. 遗留问题](#7-遗留问题)

<!-- /TOC -->
## 1. 概述
  1. 任务介绍

  - 将 darknet 的 txt 标注文件转换为 YAML 格式并存储
  - 将 labelme 的 xml 标注文件转换为 YAML 格式并存储

  2. 任务等级、周期

  - 等级：**基础**
  - 周期：*1~2日内*

## 2. 目的

  1. __掌握__ 文本文件逐行读取，解析数据
  2. __掌握__ XML文件内容读取，解析数据


## 3. 环境要求

  - ubuntu 18.04
  - python 3.6
  - pyyaml、lxml、Pillow
  - 测试数据：
    - darknet：/opt/darknet/train-0615/images
    - labelme：/var/www/html/labelme/Annotations/TN-images

    ```
    pip install pyyaml lxml Pillow
    ```

## 4. 技术要点

  1. darknet 标注数据格式：x,y,w,h,class；其中 x,y,w,h 皆为相对坐标或宽高，且 x,y 为矩形中心点坐标值，需获取图片大小后换算为绝对值。
  2. labelme 标注 xml 数据，注意其坐标点组织方式<object>...</object>
  3. 可通过 Pillow 库 API 读取图片大小：

  ```
  from PIL import Image

  pimg = Image.open('path-to-image.jpg')
  w, h = pimg.size
  ```

  4. YAML文件名称应与图像文件名一一对应，数据内容应至少包括以下几项：

    - 图像文件名
    - 图像分辨率，即图像宽高
    - 图像标注名称：列表
    - 不同物体名称对应的图像标注点：字典或数组


## 5. 处理方法与脚本

(任务)

## 6. 常见问题处理

(任务)

## 7. 遗留问题

(任务)
