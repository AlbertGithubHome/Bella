#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-1 14:11:09
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 设置图表中线型和颜色

import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(1, 18)
    y = 8*x + 7
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("修改图表线型个颜色")
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")

    #plt.plot(x, y, "ob")

    plt.plot(x, y, "vr")

    plt.show()


if __name__ == '__main__':
    main()


'''
'-'     实线样式
'--'    短横线样式
'-.'    点划线样式
':'     虚线样式
'.'     点标记
','     像素标记
'o'     圆标记
'v'     倒三角标记
'^'     正三角标记
'&lt;'  左三角标记
'&gt;'  右三角标记
'1'     下箭头标记
'2'     上箭头标记
'3'     左箭头标记
'4'     右箭头标记
's'     正方形标记
'p'     五边形标记
'*'     星形标记
'h'     六边形标记 1
'H'     六边形标记 2
'+'     加号标记
'x'     X 标记
'D'     菱形标记
'd'     窄菱形标记
'&#124;'    竖直线标记
'_'     水平线标记

'b'     蓝色
'g'     绿色
'r'     红色
'c'     青色
'm'     品红色
'y'     黄色
'k'     黑色
'w'     白色

'''