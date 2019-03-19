#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-03-18 17:48:05
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy切片处理

import numpy as np

def main():
    a = np.arange(10)
    print(a)
    b = slice(2, 8, 2) # slice函数所得是索引
    print(a[b])

    b = a[2:8:2]    # :得到的是子序列
    print(b)

    a = np.array([[3,2],[6,9],[7,5]])
    print(a)
    print(":")
    b = a[1:]
    print(b)


    # 这个地方需要好好记忆一下
    print("...")
    a = np.array([[1,2,3],[3,4,5],[4,5,6]])
    print (a[...,1])   # 第2列元素
    print (a[1,...])   # 第2行元素
    print (a[...,1:])  # 第2列及剩下的所有元素




if __name__ == '__main__':
    main()
