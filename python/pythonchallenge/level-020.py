#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-06-05 15:16:56
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 20 of python challenge
# 
# 思路：一张围栏的照片，照片上是金属网，有一个告示牌，上面写着private property beyond this fence，围墙外面的私有财产？
#       看到这里并不知道是什么意思，然后标题是go away!图片下方有一个提示为ut inspecting it carefully is allowed.
#       线索仅限于此，打开源码也没有发现新的信息，图片的名字是unreal.jpg。好像暗示了图片的内容是假的？
#       
#       真正的解题从现在开始，一开始使用火狐查看response一直没有找到所谓的的Content-Range，直到使用了QQ浏览器才看到原来是图片的
#       response才包含Content-Range，也就是需要查看unreal.jpg的response，内容为Content-Range bytes 0-30202/2123456789
#       这里涉及到断点续传的知识，参考http://www.liqwei.com/network/protocol/2011/886.shtml，也就是请求的时候需要在请求信息中加入Range
#       这里写一个request_by_range函数用来根据Range请求信息，之后使用'Range':'bytes=30202-30302'访问得到错误
#       requests.exceptions.ContentDecodingError: ('Received response with content-encoding: gzip, but failed to decode it.'
#       参考网址https://segmentfault.com/q/1010000002538867修改请求头信息添加'Accept-Encoding': ''解决了
#       接下来遇到的一个问题蒙圈了，无论我怎么修改Range 都返回错误416 - Requested Range Not Satisfiable
#       纠结了好几天终于意识到，请求的网址错误了，应该访问/pc/hex/unreal.jpg而不是/pc/hex/idiot2.html，这样根据Content-Range的范围
#       依次尝试可以得到
#       bytes=30203-
#       b"Why don't you respect my privacy?\n"
#       bytes=30237-
#       b'we can go on in this way for really long time.\n'
#       bytes=30284-
#       b'stop this!\n'
#       bytes=30295-
#       b'invader! invader!\n'
#       bytes=30313-
#       b'ok, invader. you are inside now. \n'
#       bytes=30347-
#       b''
#       由上面的信息可以看出，invader是一个关键点，到达30347时后面的信息已经没有了
#       然后调转方向从后往前尝试得到：
#
#       bytes=2123456789-
#       b'esrever ni emankcin wen ruoy si drowssap eht\n'
#       bytes=2123456743-
#       b'and it is hiding at 1152983631.\n'
#       从这个结果可以得到两个信息，the password is your new nickname in reverse，也就是密码为invader反转redavni
#       另一信息就是真正的数据可能是隐藏在1152983631位置，尝试读取得到：
#       
#       b'PK\x03\x04\x14\x00\t\x00\x08\x00;\xa7\xaa2\xac\xe5f\x14...
#       据高人所说前四个字节就能看出是一个zip文件，我是看不出来，我只能看出bz2，类似这种b'BZh91AY&SYA\xaf\x82\r\x00...
#       
#        将得到的bytes数据写入文件，然后利用zip库附带之前得到的密码redavni，就可以解压文件
#        zip_file.extractall('./challenge20', pwd=bytes("redavni", "utf8" ))
#        解压完成后得到两个文件 package.pack 和 readme.txt
#       
#       其中readme.txt中的内容为:
#       Yes! This is really level 21 in here. 
#       And yes, After you solve it, you'll be in level 22!
#       Now for the level:
#       
#       * We used to play this game when we were kids
#       * When I had no idea what to do, I looked backwards.
#       
#       至此第20关解答完毕，并且还莫名其妙的进入了第21关
#       
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/hex/idiot2.html
#       3. next level url : package.pack 下一关就只有这个文件
#       4. curlevel username:butter password:fly
#

import requests
import zipfile


# level url
level_url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'


def request_by_range(start, end):
    print('bytes={0}-{1}'.format(start,end))
    response = requests.get(level_url, auth=('butter', 'fly'), headers={'Accept-Encoding': '','Range':'bytes={0}-{1}'.format(start,end)});
    print(response.headers)
    print(response.content[0:100])
    return response.content;

def main():
    request_by_range(0, 30202)
    request_by_range(30203, '')
    request_by_range(30237, '')
    request_by_range(30284, '')
    request_by_range(30295, '')
    request_by_range(30313, '')
    request_by_range(30347, '')

    request_by_range(2123456789, '')
    request_by_range(2123456743, '')

    file_data = request_by_range(1152983631, '')
    with open('./challenge20.zip', 'wb') as file:
        file.write(file_data)

    zip_file = zipfile.ZipFile("challenge20.zip");
    zip_file.extractall('./challenge20', pwd=bytes("redavni", "utf8" ))

if __name__ == '__main__':
    main()

# 完整的打印信息
'''
bytes=0-30202
{'Date': 'Thu, 21 Jun 2018 09:50:03 GMT', 'Content-Range': 'bytes 0-30202/2123456789', 'Transfer-Encoding': 
'chunked', 'Content-Type': 'image/jpeg', 'Server': 'lighttpd/1.4.35'}
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xe1\x00\x16Exif\x00\x00MM\x00*\x00\x00
\x00\x08\x00\x00\x00\x00\x00\x00\xff\xdb\x00C\x00\x05\x03\x04\x04\x04\x03\x05\x04\x04\x04\x05\x05\x05\x06\x07
\x0c\x08\x07\x07\x07\x07\x0f\x0b\x0b\t\x0c\x11\x0f\x12\x12\x11\x0f\x11\x11\x13\x16\x1c\x17\x13\x14\x1a\x15\x11
\x11\x18!\x18\x1a\x1d\x1d\x1f'
bytes=30203-
{'Transfer-Encoding': 'chunked', 'Content-Type': 'application/octet-stream', 'Server': 'lighttpd/1.4.35', 
'Date': 'Thu, 21 Jun 2018 09:50:04 GMT', 'Content-Range': 'bytes 30203-30236/2123456789', 'Content-Transfer-Encoding': 'binary'}
b"Why don't you respect my privacy?\n"
bytes=30237-
{'Transfer-Encoding': 'chunked', 'Content-Type': 'application/octet-stream', 'Server': 'lighttpd/1.4.35', 
'Date': 'Thu, 21 Jun 2018 09:50:05 GMT', 'Content-Range': 'bytes 30237-30283/2123456789', 'Content-Transfer-Encoding': 'binary'}
b'we can go on in this way for really long time.\n'
bytes=30284-
{'Transfer-Encoding': 'chunked', 'Content-Type': 'application/octet-stream', 'Server': 'lighttpd/1.4.35', 
'Date': 'Thu, 21 Jun 2018 09:50:05 GMT', 'Content-Range': 'bytes 30284-30294/2123456789', 'Content-Transfer-Encoding': 'binary'}
b'stop this!\n'
bytes=30295-
{'Transfer-Encoding': 'chunked', 'Content-Type': 'application/octet-stream', 'Server': 'lighttpd/1.4.35', 
'Date': 'Thu, 21 Jun 2018 09:50:06 GMT', 'Content-Range': 'bytes 30295-30312/2123456789', 'Content-Transfer-Encoding': 'binary'}
b'invader! invader!\n'
bytes=30313-
{'Transfer-Encoding': 'chunked', 'Content-Type': 'application/octet-stream', 'Server': 'lighttpd/1.4.35', 
'Date': 'Thu, 21 Jun 2018 09:50:06 GMT', 'Content-Range': 'bytes 30313-30346/2123456789', 'Content-Transfer-Encoding': 'binary'}
b'ok, invader. you are inside now. \n'
bytes=30347-
{'Date': 'Thu, 21 Jun 2018 09:50:07 GMT', 'Content-type': 'text/html; charset=UTF-8', 'Content-Length': 
'0', 'Server': 'lighttpd/1.4.35'}
b''
bytes=2123456789-
{'Transfer-Encoding': 'chunked', 'Content-Type': 'application/octet-stream', 'Server': 'lighttpd/1.4.35', 
'Date': 'Thu, 21 Jun 2018 09:50:07 GMT', 'Content-Range': 'bytes 2123456744-2123456788/2123456789', 'Content-Transfer-Encoding': 'binary'}
b'esrever ni emankcin wen ruoy si drowssap eht\n'
bytes=2123456743-
{'Transfer-Encoding': 'chunked', 'Content-Type': 'application/octet-stream', 'Server': 'lighttpd/1.4.35', 
'Date': 'Thu, 21 Jun 2018 09:50:08 GMT', 'Content-Range': 'bytes 2123456712-2123456743/2123456789', 'Content-Transfer-Encoding': 'binary'}
b'and it is hiding at 1152983631.\n'
bytes=1152983631-
{'Transfer-Encoding': 'chunked', 'Content-Type': 'application/octet-stream', 'Server': 'lighttpd/1.4.35', 
'Date': 'Thu, 21 Jun 2018 09:50:08 GMT', 'Content-Range': 'bytes 1152983631-1153223363/2123456789', 
'Content-Transfer-Encoding': 'binary'}
b'PK\x03\x04\x14\x00\t\x00\x08\x00;\xa7\xaa2\xac\xe5f\x14\xa9\x00\x00\x00\xd3\x00\x00\x00\n\x00\x15\x00readme.txt
UT\t\x00\x03"\xf6\x80B\x19\xf7\x80BUx\x04\x00\xe8\x03\xe8\x03R\x1d^\xf1\xe5\xbf\xa3\xc2\xc0]\xc2)\xfd|\xdbC\x9b
\xa5\xf6B\xc1j\x1c\x8cJ^6VE\x87\xcd\xaa\x1e\xf3\xd5P\xc4\xb5I'
[Finished in 13.1s]
'''



