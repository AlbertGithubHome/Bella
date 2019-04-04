#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-3 11:55:37
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制散点图

import numpy as np
import matplotlib.pyplot as plt

def main():
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.scatter(X, Y, s=75, c=T, alpha=.5)

    plt.xlim(-1.5,1.5),
    plt.xticks([])
    plt.ylim(-1.5,1.5),
    plt.yticks([])

    plt.show()


if __name__ == '__main__':
    main()