#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-01-04 13:40:12
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : a test for reading image pixel

from PIL import Image

def read_pixel():
    im = Image.open('./test.jpg')
    w, h = im.size
    print('width = %d, height = %d' % (w, h))

    im_pixel = im.load()
    print('im_pixel =', im_pixel[0,0])
    print('im_pixel =', im_pixel[0,1])
    print('im_pixel =', im_pixel[1,0])
    print('im_pixel =', im_pixel[1023,767])


if __name__ == '__main__':
    read_pixel()
