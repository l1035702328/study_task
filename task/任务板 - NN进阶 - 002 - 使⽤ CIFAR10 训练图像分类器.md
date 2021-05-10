# 任务板 - NN进阶 - 002 - 使⽤ CIFAR10 训练图像分类器

> Author: 杨宁 last modified：2020-09-08

## 1. 概述

1. 等级：进阶
2. 数据集：CIFAR10，含10类图像的开源数据集 [下载地址](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz) 或 [本地下载](http://192.168.10.157/cifar/cifar-10-python.tar.gz)
3. 使用 pytorch/keras 提供的数据集工具，准备训练集与测试集；或 使用自定义数据集（继承方式），准备训练集（train-set）与测试集（test-set）；
4. 图像预处理
5. 自定义神经网络，训练图像分类器
6. 使用测试集，评估训练结果
7. 周期：3日内

## 2. 环境要求

python 3.6 pytorch 1.5.1

- 使用已有conda环境

```
conda activate torch15
```

- 自建环境
~~~shell
$ conda create -n pytorch python=3.6
$ conda activate pytorch
$ conda install pytorch torchvision -c pytorch
~~~

## 3. 技术要点

1. 自定义数据集加载 cifar10 图像；
2. 自定义神经网络
    1. 网络最终输出与类别数量的对应；
    2. 使用多少层卷积网络；
    3. 全连接网络起何作用；
3. 优化器（optimizer）、损失（loss）函数的选择； 
4. 自定义 P R 计算函数，通过测试集（test-set）评估模型训练结果。

参考资料：[Training a Classifier](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html)

## 4. 训练方法和脚本

## 5. 测试方法和脚本

## 6. GPU 服务器可演示内容

## 7. 常见问题处理

## 8. 遗留问题