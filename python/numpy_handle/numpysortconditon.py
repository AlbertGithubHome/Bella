#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-22 16:05:28
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的排序与条件筛选

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)

def main():
    a = np.array([[3,7,5],[8,4,3],[2,4,9]])
    aprint(a)
    aprint(np.sort(a))          # 横轴排序
    aprint(np.sort(a, axis=0))  # 纵轴排序

    a = np.array([3, 1, 2])
    aprint(a)
    b = np.argsort(a)           # 去排序后对应的之前索引
    aprint(b)
    aprint(a[b])

    a = [3, 3, 4, 5]
    b = [4, 6, 9, 4]
    aprint(np.lexsort((b, a))) # 最后一列优先考虑
    for i in np.lexsort((b, a)):
        print(a[i], b[i])


    a = [3, 4, 2, 9, 8, 6]
    aprint(np.partition(a, 4))

    a = np.array([[3,7,5],[8,4,3],[2,4,9]])
    aprint(np.argmax(a))
    aprint(np.argmax(a, axis=0))
    aprint(np.argmax(a, axis=1))
    aprint(np.argmin(a))
    aprint(np.argmin(a, axis=1))

    a = np.array([[30,40,0],[0,20,10],[50,0,60]])
    aprint(a)
    aprint(np.nonzero(a)) # 非0数组索引

    a = np.arange(16).reshape(4, 4)
    aprint(a)
    aprint(a < 10)
    b = (np.where(a < 10))
    aprint(a[b])

    print(np.extract(a % 3 == 0, a))


if __name__ == '__main__':
    main()

'''


[Finished in 0.3s]
'''