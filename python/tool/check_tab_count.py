#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def testline(filename):
    print("\n\n" + filename + "===>")
    with open(filename, 'r' ,encoding='UTF-8') as file:
        for x in range(10):
            tab_count = 0;
            line_content = file.readline()
            for x in line_content:
                if x == '\t':
                    tab_count = tab_count + 1
            print(x, tab_count)


if __name__ == '__main__':
    testline('material_1.txt')
    testline('material_2.txt')