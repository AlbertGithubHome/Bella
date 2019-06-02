#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-6-2 10:49:37
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw a simple bar

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("各年级人数条形图")
plt.xlabel("年级")
plt.ylabel("人数")

x = [1,2,3,4,5,6]
y1 = [120,98,91,130,70,90]
y2 = [110,97,98,136,60,82]

x1 = [i*3-2 for i in x];
x2 = [i*3-1 for i in x];

plt.bar(x1, y1, color='g', width=1.0, label='男生')
plt.bar(x2, y2, color='r', width=1.0, label='女生')

plt.xticks([i+0.5 for i in x1],['%d年级' % i for i in x],size='small')

for a,b in zip(x1,y1):
    plt.text(a, b+1, str(b), ha='center', va= 'bottom',fontsize=10)

for a,b in zip(x2,y2):
    plt.text(a, b+1, str(b), ha='center', va= 'bottom',fontsize=10)

plt.legend()
plt.show()







