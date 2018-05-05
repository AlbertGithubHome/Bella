#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-04 16:30:12
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 8 of python challenge
# 
# 思路：这一关网页上看不到什么提示，打开源码后发现有一个域Area，其中包含网址../return/good.html
#       点击后发现弹出一个登陆框，要求输入用户名和密码，继续往下看就会发现网页下方的注释内容
#       <!--
#       un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#       pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
#       -->
#       这看起来就是username和password，只要解析了这段看着像十六进制的字符串应该就能通关了吧!
#       
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/def/integrity.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/good.html
#       4. username:huge password:file

import requests
#import binascii
import bz2
import re

# resource url
target_url = 'http://www.pythonchallenge.com/pc/def/integrity.html'

def get_login_content():
    login_data = requests.get(target_url).content
    content = login_data.decode('utf-8')
    #print(content)
    return re.findall(r'\'(.+)\'', content)

def str2bytes(str_content):
    result_list = [];
    pos = 0
    str_content = str_content.replace("\\n", "\n").replace("\\t", "\t").replace("\\r", "\r")
    content_len = len(str_content)
    while pos < content_len:
        if str_content[pos] == '\\' and pos + 3 < content_len and str_content[pos + 1] == 'x':
            sub_str = str_content[pos + 2: pos + 4]
            result_list.append(int(sub_str, 16))
            pos = pos + 4
        else:
            result_list.append(ord(str_content[pos]))
            pos = pos + 1
    return bytes(result_list)


def main():
    login_list = get_login_content()
    username_bytes = str2bytes(login_list[0]);
    password_bytes = str2bytes(login_list[1]);
    print("username bytes:", username_bytes)
    print("password bytes:", password_bytes)

    print("username:", bz2.decompress(username_bytes))
    print("password:", bz2.decompress(password_bytes))


if __name__ == '__main__':
    main()

def test():
    login_list = get_login_content()
    print(login_list[0])
    login_list[0]
    # 这三种处理结果一致
    print(bytes(map(ord, login_list[0])))
    print(bytes(login_list[0], "utf-8"))
    print(login_list[0].encode('ascii'))
    #BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084
    #b'BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\\x06\\xbe\\x084'
    #b'BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\\x06\\xbe\\x084'
    #b'BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\\x06\\xbe\\x084'

    # 两个字节
    for x in '\xaf\x82':
        print(ord(x))

    # 八个字节
    cc = '\\xaf\\x82'
    for x in cc:
        print(ord(x))

    # 后续看一下binascii库和fromhex
    print(binascii.b2a_hex('A'.encode('ascii')))
    print(int(bytes.fromhex(sub_str), 16))

# 解析bytes数组的结果，可是费老劲了
'''
username bytes: b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password bytes: b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
[Finished in 0.8s]
'''

# 解析最后的结果
'''
username bytes: b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password bytes: b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
username: b'huge'
password: b'file'
[Finished in 0.8s]
'''