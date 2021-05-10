# 任务板 - 基础 - 图片及标注文件整理

> author：杨宁
Last modified：2020-07-22

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [任务板 - 基础 - 图片及标注文件整理](#任务板-基础-图片及标注文件整理)
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

  - 将多个图片数据集文件夹下的图片文件（格式包括 jpg、png 等），按统一编号方式，整理至 Images 文件夹中；
  - 将图片文件对应的标注文件（格式包括 txt、xml 等），按统一编号方式，整理至 Annos 文件夹；
  - 除所在文件夹不同，相同编号图片与标注文件一一对应。

  3. 任务等级、周期

  - 等级：**基础**
  - 周期：*1~2日内*

## 2. 目的

  1. __掌握__ python 文件处理的一般方法


## 3. 环境要求

  - ubuntu 18.04
  - python 3.6
  - 测试数据：/opt/ocr-data/ctw1500/train/、/opt/ocr-data/ctw1500/test/

## 4. 技术要点

  5. python 列举文件夹下特定类型文件（如`.jpg`）方法的区别：`os.listdir()`, `glob.glob()`；
  5. 格式化字符串自动编排图片文件名：`f"{idx:05d}"` or `"%05d" % idx`；
  5. 文件名称排序`sorted()`：字符串方式或整数方式排序；
  5. 检测文件/文件夹是否存在，文件夹不存在则新建；
  6. 使用`shutil`工具包拷贝/移动文件。


## 5. 处理方法与脚本

```python
# coding=utf-8
import os
from shutil import copyfile
import glob
import re


class EnvManage:
    def __init__(self, img_file_path, target_file_path, img_dis_path_dir, target_dis_path_dir):
        self.img_file_path = img_file_path
        self.target_file_path = target_file_path
        self.img_dis_path_dir = img_dis_path_dir
        self.target_dis_path_dir = target_dis_path_dir

    def windows_dispose(self):
        image_file_sort = sorted(glob.glob(self.img_file_path))
        target_file_sort = sorted(glob.glob(self.target_file_path))
        image_file_re = re_widows(image_file_sort, self.img_dis_path_dir, ".jpg")
        target_file_re = re_widows(target_file_sort, self.target_dis_path_dir, '.txt')
        print(image_file_re)
        file_mkdir(self.img_dis_path_dir)
        for i, j in zip(image_file_sort, image_file_re):
            if os.path.exists(j):
                print("{}文件已存在".format(j))
            else:
                copyfile(i, j)
        file_mkdir(self.target_dis_path_dir)
        for i, j in zip(target_file_sort, target_file_re):
            if os.path.exists(j):
                print("{}文件已存在".format(j))
            else:
                copyfile(i, j)

    def linux_dispose(self):
        image_file_sort = sorted(glob.glob(self.img_file_path))
        target_file_sort = sorted(glob.glob(self.target_file_path))
        image_file_re = re_linux(image_file_sort, self.img_dis_path_dir, ".jpg")
        target_file_re = re_linux(target_file_sort, self.target_dis_path_dir, '.txt')
        print(image_file_re)
        file_mkdir(self.img_dis_path_dir)
        for i, j in zip(image_file_sort, image_file_re):
            if os.path.exists(j):
                print("{}文件已存在".format(j))
            else:
                copyfile(i, j)
        file_mkdir(self.target_dis_path_dir)
        for i, j in zip(target_file_sort, target_file_re):
            if os.path.exists(j):
                print("{}文件已存在".format(j))
            else:
                copyfile(i, j)


def re_widows(file_name_list, path_dir, suffix):
    file_name_list_re = []
    for file_name in file_name_list:
        file_name_list_re.append(
            path_dir + "\\" + "%05d" % (int(re.findall(r"\\(\d+)%s" % suffix, file_name)[0])) + suffix)
    return file_name_list_re


def re_linux(file_name_list, path_dir, suffix):
    file_name_list_re = []
    for file_name in file_name_list:
        file_name_list_re.append(
            path_dir + "/" + "%05d" % (int(re.findall(r"/(\d+)%s" % suffix, file_name)[0])) + suffix)
    return file_name_list_re


def file_mkdir(file_path):
    if os.path.exists(file_path):
        print("{}文件夹已存在".format(file_path))
    else:
        os.mkdir(file_path)
        print("{}创建成功".format(file_path))


if __name__ == '__main__':
    img_file_path = r"/guangu/text_image/*.jpg"
    target_file_path = r"/guangu/text_label_circum/*.txt"
    img_dis_path_dir = r"/guangu/image"
    target_dis_path_dir = r"/guangu/Annos"
    aa = EnvManage(img_file_path, target_file_path, img_dis_path_dir, target_dis_path_dir)
    # aa.windows_dispose()
    aa.linux_dispose()
    

```

## 6. 常见问题处理



## 7. 遗留问题

glob.glob()本身是按照默认排序的  sorted()其实可用可不用 

因为不确定linux的路径所采用的都是绝对路径 

封装思想有问题,不知道该如何更好的结构化程序,导致代码有些混乱

