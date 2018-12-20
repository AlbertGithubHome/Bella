#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# find confict

L = []
with open('1.txt', 'r') as file:
    content = file.readline()
    content = file.readline()
    while content:
        print(content[0:-1].split('\t'))
        L.append(content[0:-1].split('\t'))
        content = file.readline()

for x in range(len(L)):
    for y in range(x+1, len(L)):
        item1 = L[x]
        item2 = L[y]
        item1names = set(item2);
        if ((item1[0] >= item2[0] and item1[0] < item2[1]) or (item2[0] >= item1[0] and item2[0] < item1[1]) and
            (item1[2] in item1names or item1[3] in item1names or item1[4] in item1names)):
            print("confict line is {0} and {1}, name = {2}".format(x + 1, y + 1, item1[2] in item1names and item1[2]
                or item1[3] in item1names and item1[3] or item1[4] in item1names and item1[4]))