#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-3 12:07:25
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制等高线图

import numpy as np
import matplotlib.pyplot as plt

def init():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("等高线图")

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

def main():
    n = 256
    x = np.linspace(-3,3,n)
    y = np.linspace(-3,3,n)
    X,Y = np.meshgrid(x,y)

    plt.axes([0.025,0.025,0.95,0.95])

    plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap=plt.cm.hot)
    C = plt.contour(X, Y, f(X,Y), 8, colors='black')
    plt.clabel(C, inline=1, fontsize=10)

    plt.xticks([])
    plt.yticks([])
    plt.show()


if __name__ == '__main__':
    main()