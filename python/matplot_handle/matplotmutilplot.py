#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-4 10:39:17
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 在图表中绘制多重网格

import numpy as np
import matplotlib.pyplot as plt

def init():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("多重网格")

def main():
    init()
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.025, left=0.025, top = 0.975, right=0.975)

    plt.subplot(2,1,1)
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2,3,4)
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2,3,5)
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2,3,6)
    plt.xticks([])
    plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()