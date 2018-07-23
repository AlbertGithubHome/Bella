#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-07-20 13:51:08
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 25 of python challenge
# 
# 思路：打开网页时一幅有山有水的图画，只不过被分成一格一格的，看起来就是我们常见的拼图，打开源码后发现图片的名字为lake1.jpg，
#       尝试了lake0.jpg和lake2.jpg没有打开，网页的标题是imagine how they sound，图片后面还有一行注释<!-- can you see the waves? -->
#       目前只有这么多内容，现在看标题中的imagine像是一个python库，查询后发现并不是，仅仅是想象的意思，标题的意思就是
#       想象他们是怎样发出声音的，注释的意思是你能看到波浪吗？好像听起来与波动有关，图片中也能看到波纹，继续前进无果
#
#       膜拜大神，解雇用了我说的线索，但是我却没有想到，将图片的后缀改为wav，读取其中的二进制内容转成图片，然后将lake1.wav、
#       lake2.wav……lake25.wav所生成的图片粘贴在一起就得到了下一关的url,decent，运行时间有点长
#       
#       一个wav文件有10800帧，每三帧为一像素，所以一个wav文件有3600像素（60*60），25个就是300*300。
#
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/hex/lake.html
#       3. next level url : http://www.pythonchallenge.com/pc/hex/decent.html
#       4. curlevel username:butter password:fly
#

from PIL import ImageDraw
from PIL import Image
import requests
import wave

# resource url
target_url = 'http://www.pythonchallenge.com/pc/hex/lake{0}.wav'

# 获得网站图像
def get_wav_file():
    for x in range(1,26):
        wav_data = requests.get(target_url.format(x), auth=('butter', 'fly')).content
        with open('challenge25/lake{0}.wav'.format(x), 'wb') as file:
            file.write(wav_data)

# 测试像素
def test_wav():
    wav_file = wave.open('challenge25/lake1.wav')
    print(wav_file.getnframes())


def main():
    get_wav_file();
    #test_wav()
    new_image = Image.new('RGB',(300,300))
    for x in range(25):
        wav_file = wave.open('challenge25/lake{0}.wav'.format(x + 1))
        bytes_array = wav_file.readframes(wav_file.getnframes())
        im = Image.frombytes('RGB',(60,60), bytes_array)
        new_image.paste(im, (60*(x%5), 60*(x//5)))
    new_image.show()


if __name__ == '__main__': main()

# 输出图片大小和起始位置
'''
[Finished in 42.5s]
'''