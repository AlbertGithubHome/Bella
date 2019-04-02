#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-1 14:29:50
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 添加子图，在它同一图中绘制不同的图形

import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(1, 12, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = 2*x + 6
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("显示正弦波")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")

    # 建立 subplot 网格，高为 2，宽为 2
    # 激活第一个 subplot
    plt.subplot(2,  2,  1)
    # 绘制第一个图像
    plt.plot(x, y1)
    plt.title('正弦')
    # 将第二个 subplot 激活，并绘制第二个图像
    plt.subplot(2,  2,  2)
    plt.plot(x, y2)
    plt.title('余弦')

    # 将第三个 subplot 激活，并绘制第三个图像
    plt.subplot(2,  2,  3)
    plt.plot(x, y3)
    plt.title('斜线')

    plt.show()


if __name__ == '__main__':
    main()