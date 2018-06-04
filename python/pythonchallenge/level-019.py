#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-06-04 13:39:48
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 19 of python challenge
# 
# 思路：页面中呈现着一张图片，看起来像一张地图，但是无法区分国家和地区，题目的标题是please！
#       完全看不懂是什么意思，打开源码发现图片的名字是map.jpg。说明图片确实是一张地图，但是下面的信息好像更重要
#       <!--
#       From: leopold.moz@pythonchallenge.com
#       Subject: what do you mean by "open the attachment?"
#       Mime-version: 1.0
#       Content-type: Multipart/mixed; boundary="===============1295515792=="
#       
#       It is so much easier for you, youngsters.
#       Maybe my computer is out of order.
#       I have a real work to do and I must know what's inside!
#       
#       --===============1295515792==
#       Content-type: audio/x-wav; name="indian.wav"
#       Content-transfer-encoding: base64
#       
#       UklGRvyzAQBXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YdizAQBABkAMQAtAAEADQAJA
#       ...
#       ...
#       PwRACEAGPwpADj8JQBA=
#       
#       --===============1295515792==--
#       
#       -->
#       上面的内容均为页面源码中注释的内容，看起来是一段经过转码的内容，其中有后缀.wav难道是一段音频，
#       还有一个线索是Content-transfer-encoding: base64，表明这段字母貌似是base64编码后的内容，
#       其中boundary="===============1295515792=="好像在暗示边界大小，但是我们处理过音频啊，只能想到是通过base64解码
#       然后生成二进制音频文件，来找找线索了，果然不出所料，生成的文件是一个完整的音频文件，文件中只有一个声音sorry，
#       将链接地址改为sorry.html，网页上显示内容- "what are you apologizing for?" 你为什么要道歉，因为什么而道歉，好像不对
#       这里其实丢下了一个重要线索，那就是地图，地图中大陆和海洋的颜色好像是反的，可能暗示了需要把得到的文件进行反转，于是将
#       得到的音频文件内容的每一帧反转，这次得到的音频文件包含内容you are an idiot ，其实我没听出来，真的太乱了，
#       其中idiot就是通向下一关的url，点开发现还有一个图片和一个超链接，点击进图20关，下一关的url实际是idiot2.html
#       
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/balloons.html
#       3. next level url : http://www.pythonchallenge.com/pc/hex/idiot2.html
#       4. curlevel username:butter password:fly
#

import requests
import base64
import wave
import re

# level url
level_url = 'http://www.pythonchallenge.com/pc/hex/bin.html'

def get_source_file_match_content():
    file_date = requests.get(level_url, auth=('butter', 'fly')).content
    result_list = re.findall(r'(UklGRvyz.*ADj8JQBA=)', file_date.decode('utf-8'), re.DOTALL)
    if len(result_list) > 0:
        return result_list[0]
    return ""

def main():
    result = get_source_file_match_content()
    with open('indian.wav','wb') as indian:
        wav = base64.b64decode(result)
        indian.write(wav)

    with wave.open('indian.wav','rb') as indian:
        with wave.open('indian_reverse.wav', 'wb') as indian_reverse:
            indian_reverse.setparams(indian.getparams())
            #indian_reverse.setnchannels(indian.getnchannels())
            #indian_reverse.setsampwidth(indian.getsampwidth())
            #indian_reverse.setframerate(indian.getframerate())
            for x in range(indian.getnframes()):
                indian_reverse.writeframes(indian.readframes(1)[::-1])

if __name__ == '__main__':
    main()

# 从网页中提取的编码内容
'''
UklGRvyzAQBXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YdizAQBABkAMQAtAAEADQAJA
...
...
PwRACEAGPwpADj8JQBA=
'''

