#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-05-29 14:06:06
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw a complex curve

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.1)
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("正弦波-余弦波")
plt.xlabel("x 轴", horizontalalignment='right', verticalalignment="center")
plt.ylabel("y 轴", verticalalignment="top")

#plt.figure(figsize=(8,6), dpi=100)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块
ax = plt.gca()#plt.subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.plot(x, y)
plt.show()



