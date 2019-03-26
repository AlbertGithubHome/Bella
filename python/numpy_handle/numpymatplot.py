#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-26 11:30:22
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的Matplot库的使用

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)

def main():
    x = np.arange(20)
    y = x * 2 + 3
    plt.xlabel('x asix')
    plt.ylabel('y asix')
    plt.title('this is a simple test')
    #plt.plot(x, y)
    #plt.show()


    # a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
    # for i in a:
    #     print(i)

    # fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径
    # zhfont1 = matplotlib.font_manager.FontProperties(fname="DejaVu Sans Mono.ttf")
    # plt.title("菜鸟教程 - 测试", fontproperties=zhfont1)

    # # fontproperties 设置中文显示，fontsize 设置字体大小
    # plt.xlabel("x 轴", fontproperties=zhfont1)
    # plt.ylabel("y 轴", fontproperties=zhfont1)
    # plt.plot(x,y)
    # plt.show()


    #plt.rcParams['font.family'] = ['DejaVu Sans Mono']
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("教程 - 测试中文")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    #plt.plot(x,y)
    #plt.show()

    #plt.plot(x,y, "Dg")
    #plt.show()

    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    #plt.plot(x, y)
    #plt.show()

    plt.title("正弦波叠加出方波")
    # y = 4 * np.sin(x) / np.pi + 4 * np.sin(3 * x) / np.pi / 3 \
    #     + 4 * np.sin(5 * x) / np.pi / 5 + 4 * np.sin(7 * x) / np.pi / 7
    # plt.plot(x, y)
    # plt.show()

    y1 = 4 * np.sin(x) / np.pi
    y2 = 4 * np.sin(3 * x) / np.pi / 3
    y3 = 4 * np.sin(5 * x) / np.pi / 5
    y4 = 4 * np.sin(7 * x) / np.pi / 7
    y = y1 + y2 + y3 + y4
    plt.plot(x, y1, ":")
    plt.plot(x, y2, ":")
    plt.plot(x, y3, ":")
    plt.plot(x, y4, ":")
    plt.plot(x, y)
    plt.show()

    # x =  [5,8,10]
    # y =  [12,16,6]
    # x2 =  [6,9,11]
    # y2 =  [6,15,7]
    # plt.bar(x, y, align =  'center')
    # plt.bar(x2, y2, color =  'g', align =  'center')
    # plt.title('Bar graph')
    # plt.ylabel('Y axis')
    # plt.xlabel('X axis')
    # plt.show()


    # a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
    # np.histogram(a,bins = [0,20,40,60,80,100])
    # hist,bins = np.histogram(a,bins =  [0,20,40,60,80,100])
    # aprint(hist)
    # aprint(bins)
    # plt.hist(a, bins =  [0,20,40,60,80,100])
    # plt.title("histogram")
    # plt.show()



if __name__ == '__main__':
    main()

'''
---------------->1
 [3 4 5 2 1]
---------------->2
 [  0  20  40  60  80 100]
[Finished in 9.1s]
'''