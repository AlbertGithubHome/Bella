#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-4 10:03:40
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制量场图

import numpy as np
import matplotlib.pyplot as plt

def init():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("量场图")

def main():
    init()
    n = 8
    X,Y = np.mgrid[0:n, 0:n]
    T = np.arctan2(Y-n/2.0, X-n/2.0)
    R = 10 + np.sqrt((Y-n/2.0)**2+(X-n/2.0)**2)
    U,V = R*np.cos(T), R*np.sin(T)

    plt.axes([0.025,0.025,0.95,0.95])
    plt.quiver(X,Y,U,V,R, alpha=.5)
    plt.quiver(X,Y,U,V, edgecolor='k', facecolor='None', linewidth=.5)

    plt.xlim(-1,n)
    plt.xticks([])
    plt.ylim(-1,n)
    plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()