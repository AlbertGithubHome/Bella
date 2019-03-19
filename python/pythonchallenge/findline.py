#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# find string contians <Text FontFamily="Roboto" and dont contians OutlineSize="1"





import os
import os.path

def main(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
            print("|      " * depth + "+--" + item)

            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth +1)



if __name__ == '__main__':
    main('.', 0)