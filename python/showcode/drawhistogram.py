#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-6-3 17:24:35
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw a histogram

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("分数分布直方图")
plt.xlabel("分数段")
plt.ylabel("人数")

# 分数
score = np.array([87,72,63,56,73,55,54,79,31,27,96,11,90,51,75])
# 分数段
section = [0,20,40,60,80,100]

#bins=[x for x in range(0, 100, 10)])

# plt.hist(score, bins=section)
# plt.show()

plt.hist(score, bins=section, edgecolor='b')

hist, bins = np.histogram(score, bins=section)
for a,b in zip(section, hist):
    plt.text(a+10, b+0.1, str(b), ha='center', va= 'bottom', fontsize=20)

plt.ylim(0, max(hist) + 1)
plt.show()









