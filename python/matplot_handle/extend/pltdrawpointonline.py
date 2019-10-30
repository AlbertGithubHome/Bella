#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-10-30 13:55:14
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 通过Zorder属性绘制点在线上

import numpy as np
import matplotlib.pyplot as plt

def draw_normal():
    plt.title("draw normal")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    X = np.linspace(1, 100, 10, endpoint=True)
    Y = np.random.randint(60, 100, len(X))

    plt.plot(X, Y, color ='blue', linewidth=3.5) # 画线
    plt.scatter(X, Y, 50, color ='red') # 画点
    plt.show()


def draw_point_on_line():
    plt.title("draw point on line")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    X = np.linspace(1, 100, 10, endpoint=True)
    Y = np.random.randint(60, 100, len(X))

    plt.plot(X, Y, color ='blue', linewidth=3.5, zorder=1) # 在第一层画线
    plt.scatter(X, Y, 50, color ='red', zorder=2) # 在第二层画点
    plt.show()


if __name__ == '__main__':
    #draw_normal()
    draw_point_on_line()