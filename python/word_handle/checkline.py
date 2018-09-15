#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# find string contians <Text FontFamily="Roboto" and dont contians OutlineSize="1"

import os
import os.path

contians_str = '<Text FontFamily="Roboto"'
not_contians_str = 'OutlineSize="1"'
result_file_name = 'find_result.txt'

def check_line(file_name):
    count = 0
    result_list = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        while True:
            try:
                count += 1
                content = file.readline()
                if contians_str in content and not_contians_str not in content:
                    result_list.append('{0}{1}line count = {2}'.format(file_name, '-'*(40 - len(file_name)), count));
                if not content:
                    return result_list
            except:
                result_list.append('\n{0} is not utf-8 file'.format(file_name));
                info ='\n{0} is not utf-8 file'.format(file_name)
                return result_list

def dfs_showdir(path, depth, outfile):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth + 1, outfile)
                #print("|      " * depth + "+--" + item)
            else:
                result = check_line(newitem)
                if len(result) > 0:
                    #print("|      " * depth + "+--" + newitem)
                    info = '\n'.join(result)
                    print(info)
                    outfile.write(info +'\n')

if __name__ == '__main__':
    with open(result_file_name, 'w') as outfile:
        dfs_showdir('.', 0, outfile)