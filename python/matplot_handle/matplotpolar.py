#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-4 10:47:08
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制极轴图

import numpy as np
import matplotlib.pyplot as plt

def init():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("极轴图")

def main():
    init()
    ax = plt.axes([0.025,0.025,0.95,0.95], polar=True)

    N = 20
    theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4*np.random.rand(N)
    bars = plt.bar(theta, radii, width=width, bottom=0.0)

    for r,bar in zip(radii, bars):
        bar.set_facecolor( plt.cm.jet(r/10.))
        bar.set_alpha(0.5)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.show()

if __name__ == '__main__':
    main()