#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-03-08 11:50:35
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
# @Subject  : level 33 of python challenge
#
# 思路：页面内容又还原成一张图片了，网页标题33 bottles of beer on the wall，图片内容有点壮观，满屏幕的啤酒瓶
#       中间的那个大木桶里面装的应该也是啤酒吧，查看源码时发现注释内容：
#       <!--
#       If you are blinded by the light,
#       remove its power, with its might.
#       Then from the ashes, fair and square,
#       another truth at you will glare.
#       -->
#       不太懂这句话的意思，又发现图片的名字是beer1.jpg，所以尝试访问beer2.jpg，可以打开并且上面显示no，png
#       难道是让我访问png图片，于是尝试打开beer2.png图片，发现中间有一个比较模糊的字母X
#
#       然后获取所有的像素值，图片是一张灰度图，每个像素点只有一个数值，通过im.getdata()获取所有数值
#       统计每个像素出现的次数，然后累加求和，发现每隔一个像素，就能够开方成整数
#       然后倒着考虑就是每次去掉最亮的两个像素值，剩下的像素个数正好是个平方数
#       每次将这些像素生成正方形图片，然后等于最大像素值的像素点设置成白色，否则设置成黑色色，然后会得到
#       33张图片，这些图片上有些带有线框，组合在一起就是 gremlins ，这就是下一关的通关密码，也就是一个临时结束点
#       后面的内容还没有更新
#
#
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/rock/beer.html
#       3. next level url : http://www.pythonchallenge.com/pc/rock/gremlins.html
#       4. curlevel username:kohsamui password:thailand
#

import requests
import numpy as np
from PIL import Image
from scipy.stats import itemfreq
from pprint import pprint

# file url
target_url = 'http://www.pythonchallenge.com/pc/rock/beer2.png'

def download_image():
    img_data = requests.get(target_url, auth=('kohsamui', 'thailand')).content
    with open('33/beer2.png', 'wb') as file:
        file.write(img_data)

def out_put_pixel():
    im = Image.open('33/beer2.png')
    im_data = np.array(list(im.getdata()))
    #print(list(im.getdata()))
    #print(len(list(im.getdata())))
    #print(im_data) #[ 1 43  7 ... 19  1  7]
    #print(im_data.shape) #(19044,)
    #print(im.getpixel((0,0)))
    #print(im.getpixel((0,1)))


    im_data_stat = itemfreq(im_data)
    #pprint(im_data_stat)
    #pprint(im_data_stat[:, 1])
    #print(im_data_stat.shape)
    #pprint([i for i in np.cumsum(im_data_stat[:, 1])])
    pprint([np.sqrt(i) for i in np.cumsum(im_data_stat[:, 1])])

    for i in range(im_data_stat.shape[0] - 1, 0, -2):
        newIm_data = im_data[np.where(im_data <= im_data_stat[i, 0])]
        idx_0 = np.where(newIm_data == newIm_data.max())
        idx_1 = np.where(newIm_data != newIm_data.max())
        newIm_data[idx_0] = 0
        newIm_data[idx_1] = 1
        size = int(np.sqrt(len(newIm_data)))
        newIm = Image.new('1', (size, size))
        newIm.putdata(newIm_data)
        newIm.save('33/%i.png' % i)

def main():
    #download_image()
    out_put_pixel()


if __name__ == '__main__': main()




# 图片像素值
'''
[ 1 43  7 ... 19  1  7]
'''

# 累加求和
'''
[39.14077158156185,
 42.0,
 52.22068555658763,
 54.0,
 60.332412515993425,
 63.0,
 67.21606950722423,
 69.0,
 70.03570517957252,
 73.0,
 73.81056834898374,
 76.0,
 76.82447526667526,
 79.0,
 79.79348344319854,
 82.0,
 82.64986388373546,
 84.0,
 84.46892919884802,
 88.0,
 89.02246907382428,
 91.0,
 91.38380600522173,
 93.0,
 93.12357381458253,
 94.0,
 94.13819628609845,
 96.0,
 96.24448036121345,
 98.0,
 98.70663604844408,
 100.0,
 100.5186549850325,
 103.0,
 103.92785959500947,
 105.0,
 105.54146104730596,
 107.0,
 107.14942836991712,
 108.0,
 109.09628774619236,
 110.0,
 110.53053876644228,
 112.0,
 112.48999955551605,
 114.0,
 114.51637437502114,
 116.0,
 116.62332528272378,
 118.0,
 118.64231959971113,
 120.0,
 120.66896867049125,
 122.0,
 122.71511724314979,
 124.0,
 124.73572062564917,
 126.0,
 126.67675398430448,
 128.0,
 128.77111477346153,
 130.0,
 130.92364186807515,
 132.0,
 137.0109484676316,
 138.0]
'''