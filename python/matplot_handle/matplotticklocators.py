#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-2 12:22:17
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制正弦波，并逐步完善细节

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def main():
    # 创建一个 8 * 6 点（point）的图，并设置分辨率为 100
    plt.figure(figsize=(8,6), dpi=100)

    # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块
    ax = plt.subplot(1, 1, 1)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    # 将x主刻度标签设置为20的倍数
    xmajorLocator   = MultipleLocator(0.5)
    #设置x轴标签文本的格式
    xmajorFormatter = FormatStrFormatter('%2.2f')
    # 设置主刻度标签的位置,标签文本的格式
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.xaxis.set_major_formatter(xmajorFormatter)


    # 在-π到π区间均匀取得256个点，分别计算
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C,S = np.cos(X), np.sin(X)

    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 2.5 （像素）的线条
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")

    # 绘制正弦曲线，使用红的、连续的、宽度为 2.5 （像素）的线条
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

    # 设置横轴的上下限
    xmin, xmax = X.min(), X.max()
    dx = (xmax - xmin) * 0.08
    plt.xlim(xmin - dx, xmax + dx)

    # 设置横轴记号
    # plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
    #plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
    #   [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    # 设置纵轴的上下限
    ymin, ymax = C.min(), C.max()
    dy = (ymax - ymin) * 0.05
    plt.ylim(ymin - dy, ymax + dy)

    # 设置纵轴记号
    # plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

    # 生成图例
    plt.legend(loc='upper left', frameon=False)
    # 以分辨率 72 来保存图片
    # savefig("../figures/exercice_2.png",dpi=72)

    # 在屏幕上显示
    plt.show()


if __name__ == '__main__':
    main()