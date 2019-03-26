#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-26 11:19:51
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的IO操作

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)

def main():
    a = np.array([[1,2],[3,4]])
    np.save('arrinfo', a)
    np.save('arrinfo2.txt', a)

    b = np.load('arrinfo.npy')
    aprint(b)

    c = np.arange(6)
    np.savez('arrinfo3', a,c)
    r = np.load('arrinfo3.npz')
    aprint(r.files)
    aprint(r['arr_1'])

    a = np.arange(0,10,0.5).reshape(4,-1)
    np.savetxt("arrinfo4.txt", a, fmt="%d", delimiter=",") # 改为保存为整数，以逗号分隔
    b = np.loadtxt("arrinfo4.txt", delimiter=",") # load 时也要指定为逗号分隔
    aprint(b)




if __name__ == '__main__':
    main()

'''
---------------->1
 [[1 2]
 [3 4]]
---------------->2
 ['arr_0', 'arr_1']
---------------->3
 [0 1 2 3 4 5]
---------------->4
 [[0. 0. 1. 1. 2.]
 [2. 3. 3. 4. 4.]
 [5. 5. 6. 6. 7.]
 [7. 8. 8. 9. 9.]]
[Finished in 0.3s]
'''