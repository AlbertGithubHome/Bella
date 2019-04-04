#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-3 16:27:26
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制灰度图

import numpy as np
import matplotlib.pyplot as plt

def init():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("灰度图")

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

def main():
    init()
    n = 10
    x = np.linspace(-3, 3, 3.5*n)
    y = np.linspace(-3, 3, 3.0*n)
    X,Y = np.meshgrid(x, y)
    Z = f(X, Y)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.imshow(Z, interpolation='bicubic', cmap='bone', origin='lower')
    plt.colorbar(shrink=.92)

    #plt.xticks([])
    #plt.yticks([])
    plt.show()


if __name__ == '__main__':
    main()