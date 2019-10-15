#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-10-3 08:59:04
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : desc relation of two k line

from enum import Enum

# 继承枚举类
class relation_type(Enum):
    NONE  = 0
    UP    = 1
    DOWN  = 3
    OPEN  = 4
    CLOSE = 5

def get_relation(pre_data, cur_data):
    if pre_data == None or cur_data == None:
        return relation_type.NONE
    elif cur_data[0] >= pre_data[0] and cur_data[1] >= pre_data[1]:
        return relation_type.UP
    elif cur_data[0] < pre_data[0] and cur_data[1] < pre_data[1]:
        return relation_type.DOWN
    elif cur_data[0] <= pre_data[0] and cur_data[1] >= pre_data[1]:
        return relation_type.OPEN
    elif cur_data[0] >= pre_data[0] and cur_data[1] <= pre_data[1]:
        return relation_type.CLOSE
    else:
        return relation_type.NONE

if __name__ == '__main__':
    print(get_relation((30,40), (31, 42)))
    print(get_relation((30,40), (31, 39)))
    print(get_relation((30,40), (29, 39)))
    print(get_relation((30,40), (29, 42)))
    print(get_relation((30,40), None))