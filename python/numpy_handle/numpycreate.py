#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-03-18 17:30:46
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 通过shape创建numpy对象

import numpy as np

def main():
    a = np.empty([2,4])
    print(a)

    a = np.zeros([2,4])
    print(a)

    a = np.ones([2,4])
    print(a)

    x =  [1,2,3]
    a = np.asarray(x, dtype =  complex)
    print (a)

    s =  b'Albert World'
    a = np.frombuffer(s, dtype =  'S1')
    print (a)


    # 使用 range 函数创建列表对象
    list=range(10)
    it=iter(list)
    # 使用迭代器创建 ndarray
    x=np.fromiter(it, dtype=int)
    print(x)

    a = np.arange(12)
    print(a)

    a = np.arange(12, 30, 2)
    print(a)


    # 等差数列
    a = np.linspace(1, 10, 5)
    print(a)

    # 等比数列
    # 默认底数是 10
    a = np.logspace(1.0,  2.0, num =  10)
    print (a)

if __name__ == '__main__':
    main()


'''
[[0.00000000e+000 0.00000000e+000 0.00000000e+000 0.00000000e+000]
 [0.00000000e+000 2.47032823e-321 1.05700345e-307 3.11521884e-307]]
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]

[1.+0.j 2.+0.j 3.+0.j]

[b'A' b'l' b'b' b'e' b'r' b't' b' ' b'W' b'o' b'r' b'l' b'd']
[0 1 2 3 4 5 6 7 8 9]
[ 0  1  2  3  4  5  6  7  8  9 10 11]
[12 14 16 18 20 22 24 26 28]

[ 1.    3.25  5.5   7.75 10.  ]

[ 10.          12.91549665  16.68100537  21.5443469   27.82559402
  35.93813664  46.41588834  59.94842503  77.42636827 100.        ]
[Finished in 0.2s]
'''