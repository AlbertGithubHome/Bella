#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-2 16:14:13
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 使用axes定义坐标轴位置，大图中画小图

import matplotlib.pyplot as plt

def main():
    plt.axes([0.1,0.1,.8,.8])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.6, 0.6, 'axes([0.1,0.1,.8,.8])', ha='center', va='center', size=25, alpha=.3)

    plt.axes([0.2,0.2,.3,.3])
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5, 0.5, 'axes([0.2,0.2,.3,.3])', ha='center', va='center', size=16, alpha=.5)

    #plt.savefig("../figures/axes.png",dpi=64)
    plt.show()

if __name__ == '__main__':
    main()