#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-2 14:06:31
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 使用gridspec布局并且设置文本信息，充分运用了切片

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def main():
    G = gridspec.GridSpec(3, 3)

    axes_1 = plt.subplot(G[0, :])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)

    axes_2 = plt.subplot(G[1,:-1])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

    axes_3 = plt.subplot(G[1:, -1])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5, 'Axes 3',ha='center',va='center',size=24,alpha=.5)

    axes_4 = plt.subplot(G[-1,0])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5, 'Axes 4',ha='center',va='center',size=24,alpha=.5)

    axes_5 = plt.subplot(G[-1,-2]) # 改成G[-1,-1]会把前面两个覆盖
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5, 'Axes 5',ha='center',va='center',size=24,alpha=.5)

    plt.show()

if __name__ == '__main__':
    main()