#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for traverse directory

__author__ = 'AlbertS'

import os
import os.path

def showdir():
    for parent, dirnames, filenames in os.walk("./"):       #分别返回:父目录、所有文件夹名字（不含路径）、有文件名字
        if '.git' not in parent and '.gita' not in dirnames:
            for filename in filenames:                        #输出文件信息
                print("parent is:" + parent)
                print("filename is:" + filename)
                print("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息

            for dirname in dirnames:                       #输出文件夹信息
                print("parent is:" + parent)
                print("dirname is:" + dirname)

def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        if '.git' not in item:
            print("|      " * depth + "+--" + item)
            
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth +1)

if __name__ == '__main__':
    dfs_showdir('.', 0)