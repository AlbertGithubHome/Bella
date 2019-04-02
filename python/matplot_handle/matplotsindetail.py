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

def test1():
    # 初始化表头-坐标轴信息
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("正弦波-余弦波")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")

    # 初始化数据信息，展示数据
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C,S = np.cos(X), np.sin(X)
    plt.plot(X, C)
    plt.plot(X, S)
    plt.show()

def test2():
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
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    # 设置纵轴的上下限
    ymin, ymax = C.min(), C.max()
    dy = (ymax - ymin) * 0.05
    plt.ylim(ymin - dy, ymax + dy)

    # 设置纵轴记号
    # plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

    # cosine 标注
    t = 2*np.pi/3
    plt.plot([t,t],[0,np.cos(t)], color ='blue',  linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.cos(t),], 50, color ='blue')
    plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                 xy=(t, np.cos(t)),  xycoords='data',
                 xytext=(-90, -50), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # sine 标注
    plt.plot([t,t],[0,np.sin(t)], color ='red',  linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.sin(t),], 50, color ='red')
    plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
                 xy=(t, np.sin(t)),  xycoords='data',
                 xytext=(+10, +30), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # 设置标签半透
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.35))

    # 生成图例
    plt.legend(loc='upper left', frameon=False)
    # 以分辨率 72 来保存图片
    # savefig("../figures/exercice_2.png",dpi=72)

    # 在屏幕上显示
    plt.show()


def main():
    test2()


if __name__ == '__main__':
    main()