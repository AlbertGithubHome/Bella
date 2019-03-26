#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-25 17:16:14
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的线性代数

import numpy as np
import numpy.matlib
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)

def main():
    a = np.array([[1,2],[3,4]])
    b = np.array([[11,12],[13,14]])
    aprint(a)
    aprint(b)
    aprint(np.dot(a,b)) # 对应行乘以对应列，放到对应坐标


    # vdot 将数组展开计算内积
    aprint(np.vdot(a,b))

    # 等价于 1*0+2*1+3*0
    aprint(np.inner(np.array([1,2,3]),np.array([0,1,0])))

    aprint(np.inner(a, b)) # 不明白啊
    '''
    1*11+2*12, 1*13+2*14
    3*11+4*12, 3*13+4*14
    '''

    a = [[1,0],[0,1]]
    b = [[4,1],[2,2]]
    aprint(np.matmul(a, b))


    a = np.array([[1,2], [3,4]]) # 对角方阵，即行列式求值 1*4 - 2*3
    aprint (np.linalg.det(a))

    x = np.array([[1,2],[3,4]]) # 求逆矩阵
    y = np.linalg.inv(x)
    aprint(x)
    aprint(y)
    aprint(np.dot(x,y))


if __name__ == '__main__':
    main()

'''
---------------->1
 [[1 2]
 [3 4]]
---------------->2
 [[11 12]
 [13 14]]
---------------->3
 [[37 40]
 [85 92]]
---------------->4
 130
---------------->5
 2
---------------->6
 [[35 41]
 [81 95]]
---------------->7
 [[4 1]
 [2 2]]
---------------->8
 -2.0000000000000004
---------------->9
 [[1 2]
 [3 4]]
---------------->10
 [[-2.   1. ]
 [ 1.5 -0.5]]
---------------->11
 [[1.0000000e+00 0.0000000e+00]
 [8.8817842e-16 1.0000000e+00]]
[Finished in 0.3s]

'''