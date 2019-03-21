#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-19 14:26:23
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的迭代器访问

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)


def main():
    aprint("")
    a = np.array([[1,2,3,4], [5, 6, 7, 8]])
    for x in np.nditer(a):
        print(x, end = ", ")
    print("\n")

    # 行优先
    aprint("")
    a = np.arange(6).reshape(2,3)
    for x in np.nditer(a.T):
        print(x, end=", " )
    print('\n')

    # 列优先
    aprint("")
    for x in np.nditer(a.T.copy(order='C')):
        print(x, end=", " )
    print('\n')

    # C风格和
    a = np.arange(0,60,5)
    a = a.reshape(3,4)
    print ('原始数组是：')
    print (a)
    print ('\n')
    print ('以 C 风格顺序排序：')
    for x in np.nditer(a, order =  'C'):
        print (x, end=", " )
    print ('\n')
    print ('以 F 风格顺序排序：')
    for x in np.nditer(a, order =  'F'):
        print (x, end=", " )
    print ('\n')

    # 对数组元素的修改，必须指定 read-write 或者 write-only 的模式。
    a = np.arange(0,60,5)
    a = a.reshape(3,4)
    print('原始数组是：')
    aprint(a)
    print('\n')
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...]=2*x
    print('修改后的数组是：')
    aprint(a)

    # 得到的值是具有多个值的一维数组，而不是零维数组
    a = np.arange(0,60,5)
    a = a.reshape(3,4)
    print('原始数组是：')
    print(a)
    print('\n')
    print('修改后的数组是：')
    for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):
       print (x, end=", " )
    print('\n')

    # 成对广播
    a = np.arange(0,60,5)
    a = a.reshape(3,4)
    print  ('第一个数组为：')
    print (a)
    print  ('\n')
    print ('第二个数组为：')
    b = np.array([1,  2,  3,  4], dtype =  int)
    print (b)
    print ('\n')
    print ('修改后的数组为：')
    for x,y in np.nditer([a,b]):
        print ("%d:%d"  %  (x,y), end=", " )
    print('\n')





if __name__ == '__main__':
    main()

'''
---------------->1

1, 2, 3, 4, 5, 6, 7, 8,

---------------->2

0, 1, 2, 3, 4, 5,

---------------->3

0, 3, 1, 4, 2, 5,

原始数组是：
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]


以 C 风格顺序排序：
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,

以 F 风格顺序排序：
0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55,

原始数组是：
---------------->4
 [[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]


修改后的数组是：
---------------->5
 [[  0  10  20  30]
 [ 40  50  60  70]
 [ 80  90 100 110]]
原始数组是：
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]


修改后的数组是：
[ 0 20 40], [ 5 25 45], [10 30 50], [15 35 55],

第一个数组为：
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]


第二个数组为：
[1 2 3 4]


修改后的数组为：
0:1, 5:2, 10:3, 15:4, 20:1, 25:2, 30:3, 35:4, 40:1, 45:2, 50:3, 55:4,

[Finished in 0.4s]
'''