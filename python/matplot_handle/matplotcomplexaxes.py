#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-2 16:21:01
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 使用axes定义坐标轴位置，大图中画小图，可以做出层叠效果

import matplotlib.pyplot as plt

def main():
    plt.axes([0.1, 0.1, .5, .5])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.1, 0.1, 'axes([0.1, 0.1, .5, .5])', ha='left', va='center',size=16, alpha=.5)

    plt.axes([0.2, 0.2, .5, .5])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.1, 0.1, 'axes([0.3, 0.3, .5, .5])', ha='left', va='center',size=16, alpha=.4)

    plt.axes([0.3, 0.3, .5, .5])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.1, 0.1, 'axes([0.3, 0.3, .5, .5])', ha='left', va='center',size=16, alpha=.3)

    plt.axes([0.4, 0.4, .5, .5])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.1, 0.1, 'axes([0.4, 0.4, .5, .5])', ha='left', va='center',size=16, alpha=.2)

    plt.axes([0.5, 0.5, .48, .48])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.1, 0.1, 'axes([0.5, 0.5, .5, .5])', ha='left', va='center',size=16, alpha=.1)

    plt.show()

if __name__ == '__main__':
    main()