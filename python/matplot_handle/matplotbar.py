#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-1 17:50:40
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制条形图

import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("条形图")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")

    x1 = [5,8,10]
    y1 = [12,16,6]
    x2 = [6,9,11]
    y2 = [6,15,7]
    plt.bar(x1, y1, align='center')
    plt.bar(x2, y2, color='g', align='center')
    plt.show()

if __name__ == '__main__':
    main()