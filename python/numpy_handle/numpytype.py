#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-03-18 16:38:53
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy可接受的常见类型

import numpy as np


def main():
    a = np.array([1,2,3,4,5], dtype = np.int_)
    print(a)

    a = np.array([1,2,3,4,5], dtype = np.bool_)
    print(a)

    a = np.array([1,2,3,4,5], dtype = np.complex)   # 复数类型
    print(a)

    a = np.array([1,2,3,4,5], dtype = np.int32, ndmin = 3) # 最小生成三维的
    print(a)


    dt = np.dtype('i1')
    print(dt)
    dt = np.dtype('i2')
    print(dt)
    dt = np.dtype('i4')
    print(dt)
    dt = np.dtype('i8')
    print(dt)

    # 字节顺序标注
    dt = np.dtype('<i4')
    print(dt)
    dt = np.dtype('>i4')
    print(dt)


    dt = np.dtype([('age',np.int8)])
    print(dt)
    a = np.array([(10,),(20,),(30,)], dtype = dt)
    print(a)
    print(a['age'])

    student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
    a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
    print(a)

    a = np.array([[1,2,3],[4,5,6]])
    print(a)
    b = a.reshape(3,2)
    print (b)

if __name__ == '__main__':
    main()

'''
[1 2 3 4 5]
[ True  True  True  True  True]
[1.+0.j 2.+0.j 3.+0.j 4.+0.j 5.+0.j]
[[[1 2 3 4 5]]]
[Finished in 0.3s]
'''