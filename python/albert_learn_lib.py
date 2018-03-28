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
