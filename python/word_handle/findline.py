#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# find string contians <Text FontFamily="Roboto" and dont contians OutlineSize="1"

import os
import os.path

def check_line(file_name):
    count = 0;
    findit = False

    with open('find_result.txt', 'a', encoding='UTF-8') as outfile:
        with open(file_name, 'r', encoding='UTF-8') as file:
            while True:
                try:
                    count += 1
                    content = file.readline()
                    if '<Text FontFamily="Roboto"' in content and 'OutlineSize="1"' not in content:
                        info = '{0}{1}line count = {2}'.format(file_name, '-'*(40 - len(file_name)), count)
                        if not findit:
                            outfile.write('\n')
                        findit = True
                        outfile.write(info + '\n')
                        print(info)

                    if not content:
                        return findit
                except:
                    info ='\n{0} is not utf-8 file'.format(file_name)
                    outfile.write(info + '\n')
                    print(info)

def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth +1)
                #print("|      " * depth + "+--" + item)
            else:
                if check_line(newitem):
                    pass #print("|      " * depth + "+--" + newitem)


if __name__ == '__main__':
    if os.path.exists('find_result.txt'):
        os.remove('find_result.txt')
    dfs_showdir('.', 0)
    #check_line('./stringresource/stringresource.txt');
    #check_line2('./test.txt');