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

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('line')

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#plt.xlabel('x轴')
#plt.ylabel('y轴')
plt.text(3.2, 0.1, 'x轴')
plt.text(0.1, 1.0, 'y轴')

plt.title('正弦波')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.plot(x, y, ":g")
plt.show()



