#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-21 13:59:25
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的各种操作：修改形状、链接分隔、改变维度

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)


def main():
    aprint("修改数组形状：")
    a = np.arange(8)
    aprint(a)
    b = a.reshape(4, 2)
    aprint(a)
    aprint(b)

    a = np.arange(9).reshape(3, 3)
    aprint(a)
    for x in a.flat:
        print(x)
    print('\n')

    a = np.arange(8).reshape(4, 2)
    aprint(a)
    aprint(a.flatten())
    aprint(a.flatten(order='F'))
    aprint(a)

    # 引用原来的元素
    aprint(a.ravel())
    aprint(a)
    b = a.ravel()
    b[0] = 100
    aprint(a)

    aprint("翻转数组:")
    a = np.arange(8).reshape(4, 2)
    aprint(a)
    aprint(np.transpose(a))
    aprint(a.T)

    a = np.arange(8).reshape(2, 2, 2) # 可以理解为中括号的滚动
    aprint(a)
    aprint(a[0])
    b = np.rollaxis(a, 2)

    print(a[0][1][1])
    print(b[1][0][1])

    print(a[0][0][1])
    print(b[1][0][0])

    a = np.arange(8).reshape(2, 2, 2) # 可以理解为中括号的互换
    aprint(a)
    aprint(a[0])
    b = np.swapaxes(a, 2, 0)

    print(a[0][1][1])
    print(b[1][1][0])

    print(a[0][0][1])
    print(b[1][0][0])


    aprint("修改数组维度:")
    a = np.arange(8)
    aprint(a.shape)

    x = np.array([[1], [2], [3]])
    y = np.array([4, 5, 6])

    # 对 y 广播 x
    b = np.broadcast(x,y)
    # 它拥有 iterator 属性，基于自身组件的迭代器元组

    print ('对 y 广播 x：')
    r,c = b.iters

    # Python3.x 为 next(context) ，Python2.x 为 context.next()
    print(next(r), next(c))
    print(next(r), next(c))
    print('\n')
    # shape 属性返回广播对象的形状

    print('广播对象的形状：')
    aprint(b.shape)
    # 本身没有改变
    aprint(x)
    aprint(y)
    aprint(x + y)

    b = np.broadcast(x,y)
    c = np.empty(b.shape)
    print('手动使用 broadcast 将 x 与 y 相加：')
    aprint(c.shape)
    c.flat = [u + v for (u,v) in b]

    print('调用 flat 函数：')
    aprint(c)


    a = np.arange(4).reshape(1,4)
    aprint(a)
    aprint(np.broadcast_to(a,(4,4)))


    a = np.arange(4).reshape(2, 2)
    b = np.expand_dims(a, axis=0)
    aprint(a)
    aprint(b)
    c = np.expand_dims(a, axis=1)
    aprint(c)
    aprint(a.ndim)
    aprint(b.ndim)
    aprint(c.ndim)

    a = np.arange(8).reshape(2, 1, 4) #必须有一维是1
    b = np.squeeze(a) #cannot select an axis to squeeze out which has size not equal to one
    aprint(a)
    aprint(b)


    aprint("连接数组：")
    a = np.array([[1,2],[3,4]])
    aprint(a)
    b = np.array([[5,6],[7,8]])
    aprint(b)
    aprint(np.concatenate((a,b)))
    aprint(np.concatenate((a,b), axis = 1))


    aprint(np.stack((a,b), 0))
    aprint(np.stack((a,b), 1))

    aprint(np.hstack((a,b))) # 怎么看起来变成了连接
    aprint(np.vstack((a,b)))

    a = np.arange(8).reshape(2, 2, 2)
    b = a
    aprint(np.hstack((a,b)))


    aprint("分割数组：")
    a = np.arange(9)
    aprint(np.split(a, 3))
    aprint(np.split(a, [2,5]))


    a = np.arange(12).reshape(2,6)
    aprint(a)
    aprint(np.hsplit(a, 3))
    aprint(np.vsplit(a, 2))


    aprint("数组元素的添加和删除：")
    a = np.arange(6).reshape(2, 3)
    aprint(a)
    b = np.resize(a, (2, 3))
    aprint(b)
    c = np.resize(a, (1, 1))
    aprint(c)
    d = np.resize(a, (3, 3)) # 出现重复
    aprint(d)


    a = np.arange(6).reshape(2,3)
    aprint(a)
    aprint(np.append(a, [6]))
    aprint(np.append(a, [6, 7, 8]))
    aprint(np.append(a, [[6, 7, 8]], axis = 0))


    a = np.arange(6).reshape(2,3)
    aprint(a)
    aprint(np.insert(a, 4, [6]))
    aprint(np.insert(a, 2, [6, 7, 8]))
    aprint(np.insert(a, 2, [[6, 7, 8]], axis = 0))


    a = np.arange(6).reshape(2,3)
    aprint(a)
    aprint(np.delete(a, 5))
    aprint(np.delete(a, 1, axis=1))


    a = np.array([1, 2, 43, 54, 5,233, 12, 2,12, 1])
    aprint(a)
    b, i = np.unique(a, return_index=True)
    aprint(b)
    aprint(i)



if __name__ == '__main__':
    main()

'''
---------------->1
 修改数组形状：
---------------->2
 [0 1 2 3 4 5 6 7]
---------------->3
 [0 1 2 3 4 5 6 7]
---------------->4
 [[0 1]
 [2 3]
 [4 5]
 [6 7]]
---------------->5
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
0
1
2
3
4
5
6
7
8


---------------->6
 [[0 1]
 [2 3]
 [4 5]
 [6 7]]
---------------->7
 [0 1 2 3 4 5 6 7]
---------------->8
 [0 2 4 6 1 3 5 7]
---------------->9
 [[0 1]
 [2 3]
 [4 5]
 [6 7]]
---------------->10
 [0 1 2 3 4 5 6 7]
---------------->11
 [[0 1]
 [2 3]
 [4 5]
 [6 7]]
---------------->12
 [[100   1]
 [  2   3]
 [  4   5]
 [  6   7]]
---------------->13
 翻转数组:
---------------->14
 [[0 1]
 [2 3]
 [4 5]
 [6 7]]
---------------->15
 [[0 2 4 6]
 [1 3 5 7]]
---------------->16
 [[0 2 4 6]
 [1 3 5 7]]
---------------->17
 [[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
---------------->18
 [[0 1]
 [2 3]]
3
3
1
1
---------------->19
 [[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
---------------->20
 [[0 1]
 [2 3]]
3
3
1
1
---------------->21
 修改数组维度:
---------------->22
 (8,)
对 y 广播 x：
1 4
1 5


广播对象的形状：
---------------->23
 (3, 3)
---------------->24
 [[1]
 [2]
 [3]]
---------------->25
 [4 5 6]
---------------->26
 [[5 6 7]
 [6 7 8]
 [7 8 9]]
手动使用 broadcast 将 x 与 y 相加：
---------------->27
 (3, 3)
调用 flat 函数：
---------------->28
 [[5. 6. 7.]
 [6. 7. 8.]
 [7. 8. 9.]]
---------------->29
 [[0 1 2 3]]
---------------->30
 [[0 1 2 3]
 [0 1 2 3]
 [0 1 2 3]
 [0 1 2 3]]
---------------->31
 [[0 1]
 [2 3]]
---------------->32
 [[[0 1]
  [2 3]]]
---------------->33
 [[[0 1]]

 [[2 3]]]
---------------->34
 2
---------------->35
 3
---------------->36
 3
---------------->37
 [[[0 1 2 3]]

 [[4 5 6 7]]]
---------------->38
 [[0 1 2 3]
 [4 5 6 7]]
---------------->39
 连接数组：
---------------->40
 [[1 2]
 [3 4]]
---------------->41
 [[5 6]
 [7 8]]
---------------->42
 [[1 2]
 [3 4]
 [5 6]
 [7 8]]
---------------->43
 [[1 2 5 6]
 [3 4 7 8]]
---------------->44
 [[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
---------------->45
 [[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]]
---------------->46
 [[1 2 5 6]
 [3 4 7 8]]
---------------->47
 [[1 2]
 [3 4]
 [5 6]
 [7 8]]
---------------->48
 [[[0 1]
  [2 3]
  [0 1]
  [2 3]]

 [[4 5]
  [6 7]
  [4 5]
  [6 7]]]
---------------->49
 分割数组：
---------------->50
 [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
---------------->51
 [array([0, 1]), array([2, 3, 4]), array([5, 6, 7, 8])]
---------------->52
 [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
---------------->53
 [array([[0, 1],
       [6, 7]]), array([[2, 3],
       [8, 9]]), array([[ 4,  5],
       [10, 11]])]
---------------->54
 [array([[0, 1, 2, 3, 4, 5]]), array([[ 6,  7,  8,  9, 10, 11]])]
---------------->55
 数组元素的添加和删除：
---------------->56
 [[0 1 2]
 [3 4 5]]
---------------->57
 [[0 1 2]
 [3 4 5]]
---------------->58
 [[0]]
---------------->59
 [[0 1 2]
 [3 4 5]
 [0 1 2]]
---------------->60
 [[0 1 2]
 [3 4 5]]
---------------->61
 [0 1 2 3 4 5 6]
---------------->62
 [0 1 2 3 4 5 6 7 8]
---------------->63
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
---------------->64
 [[0 1 2]
 [3 4 5]]
---------------->65
 [0 1 2 3 6 4 5]
---------------->66
 [0 1 6 7 8 2 3 4 5]
---------------->67
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
---------------->68
 [[0 1 2]
 [3 4 5]]
---------------->69
 [0 1 2 3 4]
---------------->70
 [[0 2]
 [3 5]]
---------------->71
 [  1   2  43  54   5 233  12   2  12   1]
---------------->72
 [  1   2   5  12  43  54 233]
---------------->73
 [0 1 4 6 2 3 5]
[Finished in 0.3s]

'''