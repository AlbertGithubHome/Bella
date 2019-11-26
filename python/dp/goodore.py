#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-26 10:17:03
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 动态规划计算挖金矿财富自由，算法来源于小灰的算法之旅


G = [400, 500, 200, 300, 350]
P = [5, 5, 3, 4, 3]
w = 10

def F(w, P, G):
    result = [0]*(w+1)

    for i in range(len(P)):
        for j in range(w, 0, -1):
            if (j >= P[i]):
                result[j] = max(result[j], result[j-P[i]] + G[i])

    print(result[w])

F(w, P, G)