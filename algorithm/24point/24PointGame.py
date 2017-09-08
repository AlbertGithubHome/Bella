#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a solution for game fo 24 point

__author__ = 'AlbertS'


result = [{}]
def Fork(A, B):
    for a in A:
        for b in B:
            subRet = set()
            subRet.add(str(a) + "+" + str(b))
            subRet.add(str(a) + "-" + str(b))
            subRet.add(str(a) + "*" + str(b))
            subRet.add(str(a) + "/" + str(b))
            subRet.add(str(b) + "-" + str(a))
            subRet.add(str(b) + "/" + str(a))


def CalcSet(i):
    if len(result[i]) > 0:
        return result[i]

    subRet = set()
    for x in range(1, i):
        if (x & i == x):
            pass
            subRet = subRet | Fork(CalcSet(x), CalcSet(i - x))
    
    return subRet

def Point24Game(array, num = 4):
    for x in range(1, pow(2, num)):
        result.append(set())

    for x in range(0, num):
        result[pow(2, x)].append(array[x])

    for x in range(1, pow(2, num)):
        result[x] = CalcSet(x)







if __name__ == '__main__':
    Point24Game([1,2,3,4])

print(result)

t = 1
print(str(t) + "v")