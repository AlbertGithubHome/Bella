#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-22 10:26:30
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的字符串处理

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)


def main():
    a = ['234', 'sx', 3]
    b = ['2342', 'sxd', 2]
    c = ['qwer', 'ggg']
    d = ['jias', 'archive']
    e = ['Create', 'cuo guo']
    f = ['create' 'cuo']
    aprint(a + b)
    aprint(np.char.add(a, b))
    aprint(c + d)
    aprint(np.char.add(c, d))
    aprint(np.char.add(c, d).shape)
    aprint(np.char.add(e, f))
    aprint(np.char.add(e, f).shape)

    aprint(np.array(e))
    aprint(np.array(e).shape)
    aprint(np.array(f))
    aprint(np.array(f).shape)

    aprint(np.char.multiply(e, 3))
    aprint(np.char.multiply(f, 3))

    aprint(np.char.center(e, 20, '-'))


    aprint(np.char.capitalize(e))

    aprint(np.char.title(e))

    aprint(np.char.lower(e))

    aprint(np.char.upper(e))


    aprint(np.char.split(e))

    aprint(np.char.splitlines(e))

    aprint(np.char.splitlines("dhs\nfhd"))
    aprint(type(np.char.splitlines("dhs\nfhd")))

    aprint(np.char.replace(e, 'c', 'g'))

    x = np.char.encode(e, 'cp500')
    aprint(x)
    aprint(np.char.decode(x, 'cp500'))

    x = np.char.encode(e, 'utf8')
    aprint(x)
    aprint(np.char.decode(x, 'utf8'))



if __name__ == '__main__':
    main()

'''

---------------->1
 ['234', 'sx', 3, '2342', 'sxd', 2]
---------------->2
 ['2342342' 'sxsxd' '32']
---------------->3
 ['qwer', 'ggg', 'jias', 'archive']
---------------->4
 ['qwerjias' 'gggarchive']
---------------->5
 (2,)
---------------->6
 ['Createcreatecuo' 'cuo guocreatecuo']
---------------->7
 (2,)
---------------->8
 ['Create' 'cuo guo']
---------------->9
 (2,)
---------------->10
 ['createcuo']
---------------->11
 (1,)
---------------->12
 ['CreateCreateCreate' 'cuo guocuo guocuo guo']
---------------->13
 ['createcuocreatecuocreatecuo']
---------------->14
 ['-------Create-------' '------cuo guo-------']
---------------->15
 ['Create' 'Cuo guo']
---------------->16
 ['Create' 'Cuo Guo']
---------------->17
 ['create' 'cuo guo']
---------------->18
 ['CREATE' 'CUO GUO']
---------------->19
 [list(['Create']) list(['cuo', 'guo'])]
---------------->20
 [list(['Create']) list(['cuo guo'])]
---------------->21
 ['dhs', 'fhd']
---------------->22
 <class 'numpy.ndarray'>
---------------->23
 ['Create' 'guo guo']
---------------->24
 [b'\xc3\x99\x85\x81\xa3\x85' b'\x83\xa4\x96@\x87\xa4\x96']
---------------->25
 ['Create' 'cuo guo']
---------------->26
 [b'Create' b'cuo guo']
---------------->27
 ['Create' 'cuo guo']
[Finished in 0.3s]
'''