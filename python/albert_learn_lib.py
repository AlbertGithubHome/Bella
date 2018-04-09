#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-03-17 16:12:05
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : record the prcess of python library learning

# 本文主要记录python各种包和库的学习过程，方便之后学习和安装
# 
# 备注：正常安装（速度慢）：pip install 包名
# 
#       快速安装（靠镜像）：pip install -i https://pypi.doubanio.com/simple 包名


import pytesseract
# 与（ORC）光学字符识别有关，全称为Optical Character Recognition，
# 简单来说就是识别图片上的文字，一开始接触于百万英雄答题外挂，用于截取答题页面截图后，
# 分析识别图片上的文字，后来又在黑板客爬虫游戏中应用，用于动态验证码识别

from aip import AipOcr
# 同样是用于识别图片文字的，来源于百度的api。
# 如果已安装pip，执行pip install baidu-aip即可；如果已安装setuptools，执行python setup.py install即可。
# 第一次使用是在2018-03-28 20:48:36，用于和pytesseract识别图片做对比

from PIL import Image
# 一开始是在廖雪峰老师的Python教程上学到的，主要是用来处理图片的，可以做旋转、模糊二值化等等。
# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
# 由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，
# Pillow支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。
# Python 2.7安装PIL，在Debian/Ubuntu Linux下直接通过apt安装：$ sudo apt-get install python-imaging。
# Python 2.7安装PIL，Windows平台就去PIL官方网站下载exe安装包。[url](http://pythonware.com/products/pil/)
# Python 3.x安装PIL,如果安装了Anaconda，Pillow就已经可用了。否则，需要在命令行下通过pip安装：$ pip install pillow

import base64
# 这个模块也是从廖雪峰老师的Python教程上可是接触的，主要负责对字符串进行base64的编码和解码工作
# 第一次正式使用应该是做一道程序员闯关题目，其中有一道题是将一副图片的数据进行了base64的编码
# 然后进行进制转换，最后以二进制空缺的形式显示作为题目入口，想想确实有点难度
# 问题解析过程：https://blog.csdn.net/albertsh/article/details/53214913
# 解题源码：https://github.com/AlbertGithubHome/Bella/blob/master/python/1111.segmentfault.com/01decode.py
# 时间：2016年11月18日 12:04:09

from functools import reduce
# 话说这个模块我之前已经没有印象了，后来发现同样出于廖雪峰老师之手。
# 通常和map函数连用，如果你没有听过map/reduce，那么Hadoop总该听说过了吧，这两者的思想是一致的
# 第一次实际使用同样是解决上边这道题，如果不用这个库，代码会很长，用了之后代码量锐减。
# 这这个例子中主要是用它把所有的单个字母串联到一起，这种情况使用map/reduce刚刚好。
# 问题解析过程：https://blog.csdn.net/albertsh/article/details/53214913
# 解题源码：https://github.com/AlbertGithubHome/Bella/blob/master/python/1111.segmentfault.com/01decode.py
# 时间：2016年11月18日 12:04:09