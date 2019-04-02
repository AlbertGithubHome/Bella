#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-2 14:06:31
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 使用subplot布局并且设置文本信息

import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.subplot(2,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5, 'subplot(2,2,1)',ha='center',va='center',size=20,alpha=.5)

    plt.subplot(2,2,2)
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5, 'subplot(2,2,2)',ha='center',va='center',size=20,alpha=.5)

    plt.subplot(2,2,3)
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5, 'subplot(2,2,3)',ha='center',va='center',size=20,alpha=.5)

    plt.subplot(2,2,4)
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5, 'subplot(2,2,4)',ha='center',va='center',size=20,alpha=.5)

    plt.show()


if __name__ == '__main__':
    main()