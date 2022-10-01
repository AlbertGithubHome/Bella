#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def main():
    l = os.listdir(".")
    for f in l:
        file_name, ext = os.path.splitext(f)
        print(file_name, ext)
        if 'IMG_' not in file_name:
            continue

        new_name = file_name[4:12]
        print(new_name)

        if os.path.isfile(new_name+ext) :
            for x in range(10):
                new_name_extend = new_name+"_"+str(x+1)+ext
                if not os.path.isfile(new_name_extend):
                    os.rename(f, new_name_extend)
                    break;
        else:
            os.rename(f, new_name+ext)



if __name__ == '__main__':
    main()
    input()