#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-05-30 12:00:18
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw two lines in a canvas

# plt.annotate用法，参考http://www.pianshen.com/article/503810176/
# 标注箭头角度设置，参考https://matplotlib.org/gallery/userdemo/connectionstyle_demo.html

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(-np.pi, np.pi, 0.1)
# y = np.sin(x)

# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# plt.text(3.2, 0.1, 'x轴')
# plt.text(0.1, 1.0, 'y轴')
# plt.title('正弦波')

# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['bottom'].set_position(('data',0))
# ax.spines['left'].set_position(('data',0))

# plt.plot(x, y, ":g")
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.1)
ysin = np.sin(x)
ycos = np.cos(x)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.text(3.2, 0.1, 'x轴')
plt.text(0.1, 1.0, 'y轴')
plt.title('正弦-余弦')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.plot(x, ysin, ":g", label="sin")
plt.plot(x, ycos, ":r", label="cos")

# 设置横轴记号
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
   [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# 设置纵轴记号
plt.yticks([-1, -0.5, 0, 0.5, +1],
   [r'$-1$', r'$-0.5$', r'$0$', r'$0.5$', r'$+1$'])


# 选定一个x坐标进行标注
x1 = 3*np.pi/4

# 正弦值 标注
# 先通过两个点做一条垂线
plt.plot([x1,x1],[0,np.sin(x1)], color ='green', linestyle="--")
# 交点处绘制一个点
plt.scatter([x1],[np.sin(x1)], 30, color ='green')
# 绘制标注点信息
plt.annotate(r'$\sin(\frac{3\pi}{4})=\frac{\sqrt{2}}{2}$',
     xy=(x1, np.sin(x1)), xycoords='data',
     xytext=(+15, +30), textcoords='offset points', fontsize=12,
     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 余弦值 标注
plt.plot([x1,x1],[0,np.cos(x1)], color ='red', linestyle="--")
plt.scatter([x1],[np.cos(x1)], 50, color ='red')
plt.annotate(r'$\cos(\frac{3\pi}{4})=-\frac{\sqrt{2}}{2}$',
     xy=(x1, np.cos(x1)), xycoords='data',
     xytext=(-90, -40), textcoords='offset points', fontsize=12,
     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


plt.legend(loc='upper left')
plt.show()
