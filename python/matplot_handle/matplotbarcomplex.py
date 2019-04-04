#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-3 12:01:09
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制复杂条形图

import numpy as np
import matplotlib.pyplot as plt

def main():
    n = 20
    X = np.arange(n)
    Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    for x,y in zip(X,Y1):
        plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

    for x,y in zip(X,Y2):
        plt.text(x+0.4, -y-0.05, '%.2f' % y, ha='center', va= 'top')

    plt.xlim(-.5,n)
    plt.xticks([])
    plt.ylim(-1.25,+1.25)
    plt.yticks([])

    plt.show()


if __name__ == '__main__':
    main()