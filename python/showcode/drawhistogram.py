#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-6-3 17:24:35
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw a histogram bar

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("直方图")
plt.xlabel("分数段")
plt.ylabel("人数")

a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
hist, bins = np.histogram(a, bins=[0,20,40,60,80,100])
print(hist)
print(bins)

plt.hist(a, bins=[0,60,80,100])#bins=[x for x in range(0, 100, 10)])
plt.show()







