#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-3 10:11:36
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制正弦波，并涂上颜色

import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("显示正弦波")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    Y = np.sin(2*X)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.plot (X, Y+1, color='blue', alpha=1.00)
    plt.fill_between(X, 1, Y+1, color='blue', alpha=.25)

    plt.plot (X, Y-1, color='blue', alpha=1.00)
    plt.fill_between(X, -1, Y-1, (Y-1) > -1, color='blue', alpha=.25)
    plt.fill_between(X, -1, Y-1, (Y-1) < -1, color='red',  alpha=.25)

    plt.xlim(-np.pi, np.pi)
    plt.xticks([])
    plt.ylim(-3.5, 3.5)
    plt.yticks([])

    #plt.savefig('../figures/plot_ex.png',dpi=48)
    plt.show()


if __name__ == '__main__':
    main()