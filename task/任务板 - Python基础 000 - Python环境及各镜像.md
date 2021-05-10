# 任务板 - Python 各镜像环境

## 1. conda 本地安装

```
conda install --use-local [path-to-package]
```

## 2. 阿里云镜像站

官方网站：https://opsx.alibaba.com/mirror

### pypi 镜像配置

- 配置方法
linux 或 mac 在文件`~/.pip/pip.conf`中添加或修改，Windows 在`~/.pip/pip.ini`中:

```
[global]
index-url=https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```

- 相关链接
PyPI 官方首页：https://pypi.org/

## 3. conda 国内镜像

- 北京外国语大学开源软件镜像站

`~/.condarc`文件中加入如下内容：

```
channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.bfsu.edu.cn/anaconda
default_channels:
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/main
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/free
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/r
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/pro
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud
  msys2: https://mirrors.bfsu.edu.cn/anaconda/cloud
  bioconda: https://mirrors.bfsu.edu.cn/anaconda/clouda
  menpo: https://mirrors.bfsu.edu.cn/anaconda/cloud
  pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.bfsu.edu.cn/anaconda/cloud
```
