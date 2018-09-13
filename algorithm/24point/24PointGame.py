#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a solution for game fo 24 point
#example [11,5,7,9] => (5+7)*(11-9)

__author__ = 'AlbertS'
import math

result = [set()]
targetNum = 24

def Fork(A, B):
    subRet = set()
    for a in A:
        for b in B:
            subRet.add("(" + a + "+" + b + ")")
            subRet.add("(" + a + "-" + b + ")")
            subRet.add("(" + b + "-" + a + ")")
            subRet.add(a + "*" + b)
            if eval(b) != 0:
                subRet.add(a + "/" + b)
            if eval(a) != 0:
                subRet.add(b + "/" + a)
    return subRet


def CalcSet(i):
    if len(result[i]) > 0:
        return result[i]

    subRet = set()
    for x in range(1, math.ceil(i / 2)):
        if (x & i == x):
            print(i, x)
            subRet = subRet | Fork(CalcSet(x), CalcSet(i - x))

    return subRet


def Check24(strList):
    subRet = set()
    for strExp in strList:
        if eval(strExp) == targetNum:
            subRet.add(strExp)
    return subRet


def Point24Game(array, num = 4):

    for x in range(1, pow(2, num)):
        result.append(set())

    for x in range(0, num):
        result[pow(2, x)].add(str(array[x]))

    for x in range(1, pow(2, num)):
        result[x] = CalcSet(x)
        #print("length =", len(result[x]), result[x])

    finalRet = Check24(result[pow(2, num) - 1])
    if len(finalRet) > 0:
        print("have result:")
        for x in finalRet:
            print(x)
    else:
        print("haven't result!")

def StartGame():
    while(True):
        global result
        result = [set()]
        a, b, c, d = map(int, input("please input 4 numbers:").split())
        print(a, b, c, d)
        Point24Game([a, b, c, d])


if __name__ == '__main__':
    StartGame()
    #Point24Game([11,5,7,9])

