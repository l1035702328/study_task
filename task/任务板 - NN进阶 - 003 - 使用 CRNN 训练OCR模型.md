# 任务板 - NN进阶 - 003 - 使用 CRNN 训练OCR模型

> Author: 杨宁 last modified：2020-09-09

## 1. 概述

1. 等级：进阶
2. 数据集：自动生成800x32大小的含中英文文字图片 或 使用开源 OCR 训练集（如 Synthetic Text）
3. 使用 CRNN 网络，训练 OCR 文字识别
4. 使用测试集，评估训练结果
5. 周期：3日内

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

1. 自动生成训练集图片时，使用不同字体库来生成含文本图片；
2. 所有中英文文字的索引构建；
3. CTC 函数的使用。

## 4. 训练方法和脚本

## 5. 测试方法和脚本

## 6. GPU 服务器可演示内容

## 7. 常见问题处理

## 8. 遗留问题