#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-03-17 16:12:05
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : record the prcess of python library learning

# 本文主要记录python各种包和库的学习过程，方便之后学习和安装
#
# 备注：正常安装（速度慢）：pip install 包名
#
#       快速安装（靠镜像）：pip install -i https://pypi.doubanio.com/simple 包名


import pytesseract
# 与（ORC）光学字符识别有关，全称为Optical Character Recognition，
# 简单来说就是识别图片上的文字，一开始接触于百万英雄答题外挂，用于截取答题页面截图后，
# 分析识别图片上的文字，后来又在黑板客爬虫游戏中应用，用于动态验证码识别
# pip install pytesseract

from aip import AipOcr
# 同样是用于识别图片文字的，来源于百度的api。
# 如果已安装pip，执行pip install baidu-aip即可；如果已安装setuptools，执行python setup.py install即可。
# 第一次使用是在2018-03-28 20:48:36，用于和pytesseract识别图片做对比

from PIL import Image
# pip install Pillow
# 一开始是在廖雪峰老师的Python教程上学到的，主要是用来处理图片的，可以做旋转、模糊二值化等等。
# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
# 由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，
# Pillow支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。
# Python 2.7安装PIL，在Debian/Ubuntu Linux下直接通过apt安装：$ sudo apt-get install python-imaging。
# Python 2.7安装PIL，Windows平台就去PIL官方网站下载exe安装包。[url](http://pythonware.com/products/pil/)
# Python 3.x安装PIL,如果安装了Anaconda，Pillow就已经可用了。否则，需要在命令行下通过pip安装：$ pip install pillow
#
# 补充一下由bytes数组直接转换成Image对象的方法，时间2018-05-03 13:53
#    从网上下载图片bytes，直接转换成Image对象
#    from PIL import Image
#    import requests
#    import io
#
#    image_data = requests.get(target_url).content
#    stream = io.BytesIO(image_data)
#    img = Image.open(stream)
#    img.show();
#
# gif图像取每一帧的图像：
#    for frame in range(img.n_frames):
#        img.seek(frame)
#
# 快速获得图像的轮廓：
# left, top, right, bottom = img.getbbox()
#
# 获取像素点
# img.getpixel((x, y))
#
# 补充时间：2018-07-20 15:03:26，Python challenge 25
# 粘贴图片，将图片part_img粘贴到图片new_image的(x,y)坐标处
# new_image.paste(part_img, x, y)#
#
# 补充时间：2018-12-20 13:47:46，Python challenge 27
# 获得GIF图像的调色板
# img = Image.open("challenge27/zigzag.gif")
# palette = img.getpalette()
#
# 补充时间：2018-12-28 12:15:45，Python challenge 30
# 可以将图片颠倒，旋转
# img = img.transpose(Image.FLIP_LEFT_RIGHT)
# img = img.transpose(Image.ROTATE_90)

import base64
# 这个模块也是从廖雪峰老师的Python教程上可是接触的，主要负责对字符串进行base64的编码和解码工作
# 第一次正式使用应该是做一道程序员闯关题目，其中有一道题是将一副图片的数据进行了base64的编码
# 然后进行进制转换，最后以二进制空缺的形式显示作为题目入口，想想确实有点难度
# 问题解析过程：https://blog.csdn.net/albertsh/article/details/53214913
# 解题源码：https://github.com/AlbertGithubHome/Bella/blob/master/python/1111.segmentfault.com/01decode.py
# 时间：2016年11月18日 12:04:09

from functools import reduce
# 话说这个模块我之前已经没有印象了，后来发现同样出于廖雪峰老师之手。
# 通常和map函数连用，如果你没有听过map/reduce，那么Hadoop总该听说过了吧，这两者的思想是一致的
# 第一次实际使用同样是解决上边这道题，如果不用这个库，代码会很长，用了之后代码量锐减。
# 这这个例子中主要是用它把所有的单个字母串联到一起，这种情况使用map/reduce刚刚好。
# 很奇怪map这个函数为什么不在functools中
# 问题解析过程：https://blog.csdn.net/albertsh/article/details/53214913
# 解题源码：https://github.com/AlbertGithubHome/Bella/blob/master/python/1111.segmentfault.com/01decode.py
# 时间：2016年11月18日 12:04:09

import string
# 之前应该使用过这个库，不过已经忘记了什么时间使用过，最近一次使用时间(2018-04-13 13:45:26)
# 目的是参加一个Python Challenge的第1关，其中有一个字符串映射的过程，本来我是使用map/reduce解决的
# 转换后提示内容告诉我可以使用函数string.maketrans()建立转换表，但是这道题目的版本应该有点早
# Python3.4已经没有string.maketrans()了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans()
# maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式
# 第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。两个字符串的长度必须相同，为一一对应的关系
# 但是还有一点，我发现即使不使用import string，也可以调用函数str.maketrans()，现在还没弄明白原因。
#
# 26个字母循环转换方法
# def auto_trans(src_str):
#     for x in range(26):
#         trans_table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'[x:x+26])
#         print(src_str.translate(trans_table))

import requests
# pip install requests
# 从开始了解爬虫时接触了这个库，对于发送get、post请求非常方便，最近一次使用时间是(2018-04-14 16:01:15)
# 目的是参加一个Python Challenge的第2关，其中有一步是为了获取网页内容所以引入了requests库，直接发送get请求
# response = requests.get(target_url)即可，获取内容直接response.content就能得到
# 之前还用urllib，不过相比较来说还是这个比较简单，不过需要单独安装pip install requests，限制大了一些
# requests 是用Python语言编写，基于 urllib，采用 Apache2 Licensed 开源协议的 HTTP 库。
# 它比 urllib 更加方便，可以节约我们大量的工作，完全满足 HTTP 测试需求。
# requests 的哲学是以 PEP 20 的习语为中心开发的，所以它比 urllib 更加 Pythoner。更重要的一点是它支持 Python3 哦！
#    Beautiful is better than ugly.(美丽优于丑陋)
#    Explicit is better than implicit.(清楚优于含糊)
#    Simple is better than complex.(简单优于复杂)
#    Complex is better than complicated.(复杂优于繁琐)
#    Readability counts.(重要的是可读性)
#
# request库断点续传的代码，Range参数需要加入到header中
#    requests.get(url, auth=('butter', 'fly'), headers={'Accept-Encoding': '','Range':'bytes=0-1023'});

import urllib
from urllib.request import urlopen
from urllib.parse import urlencode
import urllib.parse
# 这个网络请求库接触较早，第一个图片爬虫就使用了这个库，当时还没有看过多少Python代码，基本上是刚接触Python的时候
# urllib模块是python自带的，直接调用就好，相比于requests来说的好处是不用安装，不过使用起来麻烦一点
# 在网上找到一篇比较python3 urllib和requests模块区别的文章https://www.cnblogs.com/znyyy/p/7868511.html，说的比较好
# 不过总体来说就是越方便的库，就越失去了灵活性，对于特殊情况不太好处理
#
# urllib+正则：无第三方依赖
# requests+BeautifulSoup：library
# scrapy：框架
#
# 从上往下抽象程度增加，方便程度增加。“路怎么走，你们自己选啊。”
#
# 今天(2018-05-30 17:03:34)使用了urllib库中的一个函数，可以将%26SY%94%3A%E2I%00%00形式的内容直接转换成bytes数组，如下
#   import urllib.parse
#   cookies_str = '%26SY%94%3A%E2I%00%00'
#   cookies_bytes = urllib.parse.unquote_to_bytes(cookies_str.replace('+',' '))
#   print(cookies_bytes)

import re
# 开始接触Python的时候就用过这个正则表达式库，不过总是一知半解，用的时候找到之前的代码一粘贴就结束了
# 结果今天（2018-04-16 17:04:17）在使用正则表达式解析网页（做python challenge）时把自己给坑了
# 原来我一直没弄清楚匹配函数的区别，导致我使用了re.match来匹配所有符合条件的子串，结果悲剧了，一直没结果
# 在此特别记录一下匹配函数的区别，防止以后再犯错误
# re.match(pattern, string[, flags]): 从首字母开始开始匹配，string如果包含pattern子串，则匹配成功，返回Match对象，
#   失败则返回None，若要完全匹配，pattern要以$结尾。
#
# re.search(pattern, string[, flags]) : 若string中包含pattern子串，则返回Match对象，否则返回None，
#   注意，如果string中存在多个pattern子串，只返回第一个。
#
# re.findall(pattern, string[, flags]): 返回string中所有与pattern相匹配的全部字串，返回形式为数组。
#
# re.finditer(pattern, string[, flags]): 返回string中所有与pattern相匹配的全部字串，返回形式为迭代器。
#
# 2018年5月9日补充，参考：https://www.cnblogs.com/pigwan7/p/7814777.html
#
# 1、.(句点)匹配除了换行之外的所有一个字符， .*(点-星)匹配除了换行外的所有字符
# >>> r=re.compile(r'.*')
# >>> r.search('How are you\nFine thank you and you\nI am fine too').group()
# 'How are you'
#
# 这个例子可以看出.*(点-星)匹配除了换行外的所有字符，但无法匹配换行符，如何匹配包括换行符的所有字符呢
#
# 2、通过传入re.DOTALL或者re.S作为re.compile()的第二个参数
# >>> r=re.compile(r'.*',re.DOTALL)
# >>> r.search('How are you\nFine thank you and you\nI am fine too').group()
# 'How are you\nFine thank you and you\nI am fine too'
#
# >>> r=re.compile(r'.*',re.S)
# >>> r.search('How are you\nFine thank you and you\nI am fine too').group()
# 'How are you\nFine thank you and you\nI am fine too'
#
# 3、通过  (.|\n)*  正则表达式来匹配所有字
# >>> r=re.compile(r'(.|\n)*')
# >>> r.search('How are you\nFine thank you and you\nI am fine too').group()
# 'How are you\nFine thank you and you\nI am fine too'
#
# 4、除了re.DOTALL外，re.IGNORCASE(等价于re.I),re.MULTILINE(re.M)，也是很有用的参数，re.IGNORCASE可以忽略大小写
# >>> r=re.compile(r'hello',re.I)
# >>> r.findall('Hello hello world heLLo')
# ['Hello', 'hello', 'heLLo']
#
# 2018-05-14补充，参考https://blog.csdn.net/lwnylslwnyls/article/details/8901273
# Python对标准正则表达式增加的扩展功能——命名组
# 按连续相同的数字分组print(re.findall(r'((?P<word>\d)(?P=word)*)', '111221233334'))
# 结果: [('111', '1'), ('22', '2'), ('1', '1'), ('2', '2'), ('3333', '3'), ('4', '4')]


import pickle
# 这个库我确信之前没有用过，今天（2018-04-25 20:20:20）参加python challenge时第一次使用，
# 结果发现很早以前就在python教程里看过了！这个库的作用是对python对象进行序列化，序列化之后就可以保存到文件，
# 同时可以通过反序列化将文件中内存重新还原成与原来的对象，之前看这个库的时候肯定只是看看，没有写代码，要不然不能
# 一点印象也没有，反序列化的函数有pickle.load(file)和pickle.loads(bytes)，前者的参数是一个打开的文件，而后者就是
# 一个bytes数组，比如request返回的对象content，配合使用可以直接将网络资源反序列化

import zipfile
# 这个库确实是我第一次使用，今天（2018-05-02 12:11:59）参加python challenge用来解压一个zip文件
# 其实这个库除了解压还有很多其他的操作，都是关于zip文件的，参考https://www.cnblogs.com/sun-haiyu/p/7082063.html
# 最常用法：zip_file = zipfile.ZipFile('channel.zip') 打开zip文件
# zip_file.extractall('./channel')将zip文件全部解压到目录'./channel'中
# 解压带密码的zip文件：
# zip_file.extractall('./challenge20', pwd=bytes("password", "utf8" ))
#
# zip文件的数据开头为：b'PK\x03\x04\x14\x00...

import bz2
# 前几天使用了zip压缩文件，今天（2018-05-04 16:30:12）又接触到了新的压缩类型bz2，这是一种常用的压缩格式
# 同样是在进行python challenge时使用到的，根据我的推断应该是压缩的字节流起始字节是BZ，因为我解压的两个bytes都是这样的
#
#    username_bytes = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#    password_bytes = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
#
#    print("username:", bz2.decompress(username_bytes))
#    print("password:", bz2.decompress(password_bytes))
#
# 使用非常方便，直接调用方法decompress，将需要解压的内容传入即可
# 在python challenge第8关，使用到了bz2，并且写了一个函数str2bytes，用来解决将文件中的BZh91AY&SYA\xaf\x82\r字符串，转成16进制
# 原来花费了很多时间都没有搞定，这次自定义实现了
#
# def str2bytes(str_content):
#    result_list = [];
#    pos = 0
#    str_content = str_content.replace("\\n", "\n").replace("\\t", "\t").replace("\\r", "\r")
#    content_len = len(str_content)
#    while pos < content_len:
#        if str_content[pos] == '\\' and pos + 3 < content_len and str_content[pos + 1] == 'x':
#            sub_str = str_content[pos + 2: pos + 4]
#            result_list.append(int(sub_str, 16))
#            pos = pos + 4
#        else:
#            result_list.append(ord(str_content[pos]))
#            pos = pos + 1
#    return bytes(result_list)
#
# 找到了更简单的的方法：
#   str_content = 'BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\x06\\xbe\\x084'
#   bytes_content = bytes(str_content, "latin1")
#   print(bytes_content.decode('unicode_escape').encode('latin1'))
#
# 或者
#   import codecs
#   print(codecs.escape_decode(bytes_content)[0])
#
# 结果：
# b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# [Finished in 0.1s]
#

from PIL import ImageDraw
# 之前使用过Image这个库，最近（2018-05-08 13:37:23）在做python challenge时，涉及到一个图像处理的的操作
# 具体的用法就是使用Image库创建图片对象，然后使用ImageDraw来进行下一步的图像绘制，例如
#    img = Image.new('RGB', (width, height))
#    draw = ImageDraw.Draw(img)
#    draw.line(first_list)
#    draw.line(second_list)
#    img.show()
# 其中line函数的参数是一个数字的list，表示点的信息，具体例子参考：
# https://github.com/AlbertGithubHome/Bella/blob/master/python/pythonchallenge/level-009.py
# 也可以在图像上画点的，具体方法为：
#    draw.point([center_x, center_y])

import urllib.request
# 使用这个库的参考网上的解决方案用来解决python challenge第9关中的密码验证问题，因为网页需要验证才能打开
# 而这样的网页有不同于登录页面，其中只需要一个验证，使用requests库一直没有找到解决方法，post，get，session
# cookies都用过了也没有解决，后来偶然间发现urllib.request可以办到，于是使用了网上的代码：
#
#    # create a password manager
#    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
#
#    # Add the username and password.
#    # If we knew the realm, we could use it instead of None.
#    top_level_url = "http://www.pythonchallenge.com/pc/return/good.html"
#    password_mgr.add_password(None, top_level_url, 'huge', 'file')
#    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
#
#    # create "opener" (OpenerDirector instance)
#    opener = urllib.request.build_opener(handler)
#
#    # use the opener to fetch a URL
#    a_url = "http://www.pythonchallenge.com/pc/return/good.html"
#    x = opener.open(a_url)
#    print(x.read())
#
#    接着又有好消息，原来requests也能办到，并且更加简便：
#    login_data = requests.get(target_url, auth=('huge', 'file')).content
#
#    看来urllib.request要想真正的发挥作用还需要后续的探索了

import xmlrpc.client
import xmlrpc.server
# 这个库真的是第一次(2018-05-22 13:39:51)听说，第一次使用，居然使用了rpc，很神奇的经历，
# 之前一直以为这些分布式服务器通常用C++来写，没想到第一次使用的居然是xml版本，居然还是在Python上
# 使用方法很简单，就像调用本地对象的函数一样就可以，但是需要区分Python2.x 和Python3.x版本，两个版本有很大的不同
# 以网址'http://www.pythonchallenge.com/pc/phonebook.php'提供的服务为例
# Python2.x
#   import xmlrpclib
#   server = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
#   print server.system.listMethods()
#   print server.system.methodHelp('phone')
#   print server.phone('Bert')
#
# Python3.x
#   import xmlrpc.client
#   server = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
#   print(server.system.listMethods())
#   print(server.system.methodHelp('phone'))
#   print(server.phone('Bert'))
#
# 这些不同主要体现在创建连接服务器上，Python2.x参考https://blog.csdn.net/comprel/article/details/72633406
# 新的版本将服务器和客户端统一移动到库xmlrpc中，不需要安装，Python3.x参考https://docs.python.org/3/library/xmlrpc.html

import datetime
# 这个库不是第一次使用，今天（2018-05-24 16:08:04）记录一下简单用法，用来生成日期或处理日期格式的数据
# 比如通过年月日生成一个日期的代码：
#
#   import datetime
#   date = datetime.date(1997,12,25)
#   print(date)
#
# 结果为：1997-12-25

import calendar
# 这个库之前没有用到过，今天（2018-05-24 16:08:04）解决Python Challenge 15的时候第一次听说
# 其实就是一个日历相关的模块，使用这个模块可以简单查询一个年份是否是闰年，使用方式如下:
#
#   calendar.isleap(year)
#
# 结果为：true或者false

import wave
# 关于音频的操作之前没有接触过，今天（2018-06-04 13:39:48）参见Pyhton challenge第一次使用，其实wave本质上
# 操作的是一个二进制文件，将这个文件通过wave库打开即可使用关于音频操作的一些函数，下面的代码展示了如何将一个
# 音频文件的每一帧反转形成一个新的音频文件，其中设置参数可以通过setparams一个函数代替下面的三个指定参数:
#
#   with wave.open('indian.wav','rb') as indian:
#       with wave.open('indian_reverse.wav', 'wb') as indian_reverse:
#           indian_reverse.setparams(indian.getparams())
#           #indian_reverse.setnchannels(indian.getnchannels())
#           #indian_reverse.setsampwidth(indian.getsampwidth())
#           #indian_reverse.setframerate(indian.getframerate())
#           for x in range(indian.getnframes()):
#               indian_reverse.writeframes(indian.readframes(1)[::-1])

import zlib
# 这个库也是一个用来解压文件数据的库，今天（2018-06-21 18:11:07）解决python challenge 21时，第一次使用，
# 使用方法很类似于bz2这个库，使用zlib库解压的数据开头的连个字节为b'x\x9c'或者写成b'\x78\x9c'
# 解压方法就是decompress，直接调用就可以
# content_data = zlib.decompress(content_data);

import this
# 真的没想到this也是一个库，今天（2018-06-26 15:20:13）在结果python challenge 23时第一次听说
# import之后会自动打印出Python哲学，内容如下：
#       The Zen of Python, by Tim Peters
#
#       Beautiful is better than ugly.
#       Explicit is better than implicit.
#       Simple is better than complex.
#       Complex is better than complicated.
#       Flat is better than nested.
#       Sparse is better than dense.
#       Readability counts.
#       Special cases aren't special enough to break the rules.
#       Although practicality beats purity.
#       Errors should never pass silently.
#       Unless explicitly silenced.
#       In the face of ambiguity, refuse the temptation to guess.
#       There should be one-- and preferably only one --obvious way to do it.
#       Although that way may not be obvious at first unless you're Dutch.
#       Now is better than never.
#       Although never is often better than *right* now.
#       If the implementation is hard to explain, it's a bad idea.
#       If the implementation is easy to explain, it may be a good idea.
#       Namespaces are one honking great idea -- let's do more of those!

#import md5
import hashlib
# 这个库基本上在各个成熟点的语言中都存在，在解答Python Challenge 26关时（2018-07-23 12:14:04）第一次使用
# 有个生成数字摘要的方法，使用如下：
# if md5.md5(new_data).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b' :
#     pass
# 这样就可以判断数字摘要是否等于某个值！
# 注意在Python2.x版本需要使用import md5
# 在Python3.x版本需要使用import hashlib

from tkinter import *
from tkinter import ttk
# 这个库是做游戏开发时想显示地图阻挡颜色时查到的，主要为了做一个显示界面，用来显示各种地图阻挡信息
# 界面很简单，用各种标签设置颜色用来表现信息（2018-12-07 18:00:34）第一次使用，具体用法参考例子：
# https://github.com/AlbertGithubHome/Bella/blob/master/python/ui/colorplate.py

import keyword
# 这个库包含了python的关键字，在解答Python Challenge 27关时（2018-12-20 16:30:07）第一次使用
# 其中有一个方法用于判断是否是python关键字
# keyword.iskeyword(mystr)

import numpy
from numpy import genfromtxt
# 这个库可以说是python数据处理必学的，之前见过多次，但都是忙于解决问题，没有掌握怎么使用，在
# 解答Python Challenge 30关时（2018-12-26 16:15:42）开始学习使用方法，用于数据的处理
# 安装方法：pip install numpy
# genfromtxt可以把标准的CSV文件转为array，但是如果列数不统一，会转换失败

import operator
# 这个库里包含了运算的操作符，在解答Python Challenge 30关时（2018-12-27 11:28:32）第一次用到
# 一般使用+-*/就可以了，但是在需要函数的时候用这个库更合理一些，比如将二维list转换为一维list
# L = [[1,2], [3,4]]
# L = reduce(operator.add, L)
# L is [1, 2, 3, 4]

import xlwt
import xlrd
# 这两个库用于操作Excel表和其他类型文件的转换，据我分析应该是Excel Write 和Excel Read的缩写
# 在尝试把自己的支出记录转换成txt表格时（2019-1-6 17:04:05）时第一次使用，具体用法后续补充

from matplotlib import pyplot as plt
# 用于绘图的一个常用库，与Numpy使用可以有效的替代MatLab开源方案，也可以和图形工具包一起使用，
# 如 PyQt 和 wxPython，在系统学习Numpy使用方法时（2019-3-26 11:33:03），了解了一下，参考网址：
# http://www.runoob.com/numpy/numpy-matplotlib.html

import configparser
# 用来读取配置文件，配置文件的格式跟windows下的ini配置文件相似，可以包含一个或多个节(section),
# 每个节可以有多个参数（键=值），在看《自动化平台测试开发》一书时（2019-4-2 10:05:59）第一次发现
# 当时只是看文档，还没来得及试一下

import mpl_finance as mpf
# 这个库原来的引用方法是import matplotlib.finance as mpf（python2.2），后来从 matplotlib 独立出来成为mpl_finance
# 一般使用其中的candlestick_ochl和candlestick_ohlc函数来画股票的K线图，在研究画K线时（2019-9-24 20:27:01）第一次发现
# 本来还打算使用matplotlib自己画呢，现在来看画K线很方便了

import pandas as pd
# 分析不识潘大师(PANDAS)，纵是老手也枉然——之前偶然间看到这句话，今天（2019-9-24 20:30:37）在画K线时了解一下
# pandas是基于numpy的专业数据分析工具，可以灵活高效的处理各种数据集

import tushare as ts
# Tushare是一个免费、开源的python财经数据接口包。
# 主要实现对股票等金融数据从数据采集、清洗加工 到 数据存储的过程，
# 能够为金融分析人员提供快速、整洁、和多样的便于分析的数据，为他们在数据获取方面极大地减轻工作量，
# 使他们更加专注于策略和模型的研究与实现上，今天（2019-9-26 19:49:00）在查询股票数据时开始接触,
# 依赖pandas和lxml两个库，安装方法pip insall tushare(pip install pandas, pip install lxml)
# 后来安装时发现还需要bs4