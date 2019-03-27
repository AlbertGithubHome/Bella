#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-26 17:01:37
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 使用numpy和Matplot近似使用正弦波叠加出方波

import numpy as np
from matplotlib import pyplot as plt
import matplotlib

def main():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("正弦波叠加出方波")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")

    x = np.arange(0, 4 * np.pi, 0.1)
    y = 4 * np.sin(x) / np.pi

    for i in range(3, 3000, 2):
        y = y + 4 * np.sin(i * x) / np.pi / i
        plt.plot(x, y, ":")

    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    main()

'''

'''