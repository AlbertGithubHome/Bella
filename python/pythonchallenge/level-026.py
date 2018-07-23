#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-07-23 12:14:04
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 27 of python challenge
# 
# 思路：网页上显示的是画着两个猴子的图片，图片下方显示一行金色的字Hurry up, I'm missing the boat
#       查看源码发现标题为be a man - apologize!含义就是作为一个人需要道歉，图片引用的后面有一行注释
#       <!-- you've got his e-mail -->，好像是提醒我要给某个人发邮件道歉，源码最下面还有注释内容
#       <!--
#       Join us at the IRC: irc.freenode.net #pythonchallenge
#       -->
#       看起来和本关没有关系，前面的关卡确实有一关提到了道歉，好像还是用的RPC，我找找
#       查询后发现王志伟http://www.pythonchallenge.com/pc/hex/bin.html，在19关左右
#       注释内容让我从图片中获得邮件地址，难道让我给猴子发邮件？
#       其实19关的源码里已经提供了邮箱，就是leopold.moz@pythonchallenge.com
#       给这个邮箱发邮件，主题是Sorry，马上收到邮件回复，内容如下：
#       Never mind that.
#
#       Have you found my broken zip?
#
#       md5: bbb8b499a0eef99b52c7f13f4e78c24b
#
#       Can you believe what one mistake can lead to?
#       
#       邮件中提到了broken zip，之前的关卡level-24中确实得到了一个mybroken.zip文件
#       解压文件时报错，提示解压错误，错误信息如下：
#       File "H:\Program Files\Python\Python35-32\lib\zipfile.py", line 862, in _update_crc
#       raise BadZipFile("Bad CRC-32 for file %r" % self.name)
#       zipfile.BadZipFile: Bad CRC-32 for file 'mybroken.gif'
#       
#       邮件回复的内容提示错了一个字节，穷举解决，其中好几次都无法找到，原因可以看一下函数test_bytes的结果
#       成功解压后发现一张图片mybroken.gif，图片上的额内容为speed，结合提示Hurry up, I'm missing the boat
#       最后组成speedboat，也就是通往下一关的url
#       
#       
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/hex/decent.html
#       3. next level url : http://www.pythonchallenge.com/pc/hex/speedboat.html
#       4. curlevel username:butter password:fly
#

import zipfile
import hashlib

# 测试解压
def test_unzip():
    zip_file = zipfile.ZipFile('./challenge24/mybroken.zip')
    zip_file.extractall('./challenge24')

def test_bytes():
    mistake_byte = 168
    print(chr(mistake_byte))
    print(bytes(chr(mistake_byte), encoding='utf-8'))
    print(bytes(mistake_byte))
    print(bytes([mistake_byte]))

def change_zip():
    with open('./challenge24/mybroken.zip', 'rb') as file:
        file_data = file.read()
        for i in range(len(file_data)):
            for mistake_byte in range(256):
                new_data = file_data[:i] + bytes([mistake_byte]) + file_data[i+1:]
                if hashlib.md5(new_data).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b' :
                    with open('./challenge26/new_mybroken.zip', 'wb') as file:
                        file.write(new_data)
                    print("position: {0}, old byte: {1}, new byte : {2}".format(i, file_data[i:i+1], mistake_byte))
                    return 0

def main():
    #test_unzip();
    #change_zip();
    test_bytes();



if __name__ == '__main__': main()

# 解压报错信息
'''
  File "H:\Program Files\Python\Python35-32\lib\zipfile.py", line 934, in _read1
    self._update_crc(data)
  File "H:\Program Files\Python\Python35-32\lib\zipfile.py", line 862, in _update_crc
    raise BadZipFile("Bad CRC-32 for file %r" % self.name)
zipfile.BadZipFile: Bad CRC-32 for file 'mybroken.gif'
[Finished in 5.8s with exit code 1]
'''
# 错误的字节信息
'''
position: 1234, old byte: b'-', new byte : 168
[Finished in 3.5s]
'''

# test_bytes结果,当mistake_byte为特殊字符时，第一种方法不为一个字节
'''
¨
b'\xc2\xa8'
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
b'\xa8'
'''