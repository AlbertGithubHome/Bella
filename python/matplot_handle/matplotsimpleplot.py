#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-1 13:57:24
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 最简单的一个线形图

import numpy as np
import matplotlib.pyplot as plt

def main():

    x = np.arange(1, 18)
    y = 8*x + 7
    plt.title("Matplotlib simple demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()