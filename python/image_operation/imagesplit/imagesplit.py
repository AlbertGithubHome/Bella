#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-2-4 10:54:44
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : split images

import os
from PIL import Image

def imsplit(input_file_name, row_part, col_part):
    img = Image.open(input_file_name)
    w, h = img.size
    print('width = %d, height = %d' % (w, h))

    file_path,temp_file_name = os.path.split(input_file_name)
    file_name,ext = os.path.splitext(temp_file_name)

    avg_width_pixel = w // col_part
    avg_height_pixel = h // row_part

    for r in range(row_part):
        for c in range(col_part):
            end_width_pixel = (c + 1) * avg_width_pixel if c < col_part - 1 else w
            end_height_pixel = (r + 1) * avg_height_pixel if c < row_part - 1 else h
            box = (c * avg_width_pixel, r * avg_height_pixel, end_width_pixel, end_height_pixel)
            output_file = os.path.join(file_path, file_name + '_' + str(r) + '_' + str(c) + ext)
            print(output_file)
            img.crop(box).save(output_file, 'JPEG' if ext.lower() == '.jpg' else ext.upper()[1:])

if __name__ == '__main__':
    imsplit('./20200204080200.jpg', 3, 1);
