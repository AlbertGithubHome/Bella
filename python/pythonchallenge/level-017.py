#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-29 15:41:34
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 17 of python challenge
# 
# 思路：这次页面中有一张大图，看起来像土豆饼，然后土豆饼的左下角居然有两个小人，看着像木偶，
#       标题是eat？除此之外没有其他的提示了，不过图片的名字是cookies.jpg貌似再暗示我需要打印cookies看看，
#       先试着打印一下，只得到<RequestsCookieJar[]>，没有什么有价值的进展，看看大神的解答吧，果然和cookies有关
#       不过不是这关的cookies，而是第四关的cookies，为什么呢？因为这一关的左下角的图片是第四关的，我说怎么这么眼熟呢！
#       我们先打印cookies内容<RequestsCookieJar[<Cookie info=you+should+have+followed+busynothing... for .pythonchallenge.com/>]>
#       貌似是说在网址后面跟上busynothing，长得和原来的nothing好像，用第四关的方式解决一下，然后发现每一个页面的cookies都有内容，
#       于是连接到一起得到一个BZh9...开头的字符串，于是想起了bz2压缩，解压试试，直接转成bytes解压报错了OSError: Invalid data stream
#       然后进行转码德奥...\x92\xc4Bc\xf1w$S\x85\t\tC\xae$'，解压发现还是报错，与别人的结果对比发现结尾少了\x90',修改边界条件继续上述操作,
#       得到信息 is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.
#       给his father大打电话？his father应该值的时候莫扎特的父亲Leopold，用一下13关的服务器试试，打完电话得到的是555-VIOLIN
#       小提琴？电话555，访问violin.html，得到no! i mean yes! but ../stuff/violin.php. 访问/www.pythonchallenge.com/pc/stuff/violin.php
#       进入一个网页，页面上有一幅图，莫非是莫扎特，标题为it's me. what do you want?，卡住了，怎么办，前面还有一个提示
#       inform him that "the flowers are on their way"，通知？怎么通知，原来是把cookies中的info改为the flowers are on their way
#       通知完得到返回的结果，得到网页内容oh well, don't you dare to forget the balloons. 所以balloons就是通往下一关的url
#       这个我参加python challenge以来做过的最曲折的题目！
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/romance.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/balloons.html
#       4. username:huge password:file
#

import requests
import bz2
import re
import urllib.parse
import xmlrpc.client

level4_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
level4_url_forward = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
server_url = 'http://www.pythonchallenge.com/pc/phonebook.php'
inform_url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'

def get_source_cookies():
    cookies_date = requests.get(level4_url, auth=('huge', 'file')).cookies
    print(cookies_date)

def get_content_and_cookies(combine_url):
    response = requests.get(combine_url)
    return response.content.decode('utf8'), response.cookies;

def get_cookies_str():
    next_number = '12345'
    cookies_result = [];
    while True:
        content, cookies = get_content_and_cookies(level4_url_forward + next_number)
        #print(content, cookies)
        number_list = re.findall(r'is (\d*)', content)
        #print(number_list)
        cookies_result.append(cookies['info'])
        if len(number_list) == 0:
            break;
        next_number = number_list[0];
        #print(cookies['info'])
    #print("\n\n", cookies_result)
    return ''.join(cookies_result)

def main():
    #get_source_cookies();
    if False:
        cookies_str = get_cookies_str();
        #print(cookies_str)
        cookies_bytes = urllib.parse.unquote_to_bytes(cookies_str.replace('+',' '))
        print(cookies_bytes)
        print(bz2.decompress(cookies_bytes))

    server = xmlrpc.client.ServerProxy(server_url)
    print(server.phone('Leopold'))

    print(requests.get(inform_url, auth=('huge', 'file'), 
        headers = {'Cookie' : 'info=the flowers are on their way'}).content.decode('utf-8'))

if __name__ == '__main__':
    main()

# 打印cookies结果
'''
<RequestsCookieJar[]>
[Finished in 0.8s]
'''

# 打印第四关的cookies
'''
<RequestsCookieJar[<Cookie info=you+should+have+followed+busynothing... for .pythonchallenge.com/>]>
[Finished in 2.0s]
'''

# 中间调试内容，很长很长
'''
If you came here from level 4 - go back!<br>You should follow the obvious chain...<br><br>and the next busynothing is 44827 <RequestsCookieJar[<Cookie info=B for .pythonchallenge.com/>]>
['44827']
B
and the next busynothing is 45439 <RequestsCookieJar[<Cookie info=Z for .pythonchallenge.com/>]>
['45439']
Z
and the next busynothing is 94485 <RequestsCookieJar[<Cookie info=h for .pythonchallenge.com/>]>
['94485']
h
and the next busynothing is 72198 <RequestsCookieJar[<Cookie info=9 for .pythonchallenge.com/>]>
['72198']
9
and the next busynothing is 80992 <RequestsCookieJar[<Cookie info=1 for .pythonchallenge.com/>]>
['80992']
1
and the next busynothing is 8880 <RequestsCookieJar[<Cookie info=A for .pythonchallenge.com/>]>
['8880']
A
and the next busynothing is 40961 <RequestsCookieJar[<Cookie info=Y for .pythonchallenge.com/>]>
['40961']
Y
and the next busynothing is 58765 <RequestsCookieJar[<Cookie info=%26 for .pythonchallenge.com/>]>
['58765']
%26
and the next busynothing is 46561 <RequestsCookieJar[<Cookie info=S for .pythonchallenge.com/>]>
['46561']
S
and the next busynothing is 13418 <RequestsCookieJar[<Cookie info=Y for .pythonchallenge.com/>]>
['13418']
Y
and the next busynothing is 41954 <RequestsCookieJar[<Cookie info=%94 for .pythonchallenge.com/>]>
['41954']
%94
and the next busynothing is 46782 <RequestsCookieJar[<Cookie info=%3A for .pythonchallenge.com/>]>
['46782']
%3A
and the next busynothing is 92730 <RequestsCookieJar[<Cookie info=%E2 for .pythonchallenge.com/>]>
['92730']
%E2
and the next busynothing is 89229 <RequestsCookieJar[<Cookie info=I for .pythonchallenge.com/>]>
['89229']
I
and the next busynothing is 25646 <RequestsCookieJar[<Cookie info=%00 for .pythonchallenge.com/>]>
['25646']
%00
and the next busynothing is 74288 <RequestsCookieJar[<Cookie info=%00 for .pythonchallenge.com/>]>
['74288']
%00
and the next busynothing is 25945 <RequestsCookieJar[<Cookie info=%21 for .pythonchallenge.com/>]>
['25945']
%21
and the next busynothing is 39876 <RequestsCookieJar[<Cookie info=%19 for .pythonchallenge.com/>]>
['39876']
%19
and the next busynothing is 8498 <RequestsCookieJar[<Cookie info=%80 for .pythonchallenge.com/>]>
['8498']
%80
and the next busynothing is 34684 <RequestsCookieJar[<Cookie info=P for .pythonchallenge.com/>]>
['34684']
P
and the next busynothing is 62316 <RequestsCookieJar[<Cookie info=%81 for .pythonchallenge.com/>]>
['62316']
%81
and the next busynothing is 71331 <RequestsCookieJar[<Cookie info=%11 for .pythonchallenge.com/>]>
['71331']
%11
and the next busynothing is 59717 <RequestsCookieJar[<Cookie info=%00 for .pythonchallenge.com/>]>
['59717']
%00
and the next busynothing is 76893 <RequestsCookieJar[<Cookie info=%AF for .pythonchallenge.com/>]>
['76893']
%AF
and the next busynothing is 44091 <RequestsCookieJar[<Cookie info=g for .pythonchallenge.com/>]>
['44091']
g
and the next busynothing is 73241 <RequestsCookieJar[<Cookie info=%9E for .pythonchallenge.com/>]>
['73241']
%9E
and the next busynothing is 19242 <RequestsCookieJar[<Cookie info=%A0 for .pythonchallenge.com/>]>
['19242']
%A0
and the next busynothing is 17476 <RequestsCookieJar[<Cookie info=+ for .pythonchallenge.com/>]>
['17476']
+
and the next busynothing is 39566 <RequestsCookieJar[<Cookie info=%00 for .pythonchallenge.com/>]>
['39566']
%00
and the next busynothing is 81293 <RequestsCookieJar[<Cookie info=h for .pythonchallenge.com/>]>
['81293']
h
and the next busynothing is 25857 <RequestsCookieJar[<Cookie info=E for .pythonchallenge.com/>]>
['25857']
E
and the next busynothing is 74343 <RequestsCookieJar[<Cookie info=%3D for .pythonchallenge.com/>]>
['74343']
%3D
and the next busynothing is 39410 <RequestsCookieJar[<Cookie info=M for .pythonchallenge.com/>]>
['39410']
M
and the next busynothing is 5505 <RequestsCookieJar[<Cookie info=%B5 for .pythonchallenge.com/>]>
['5505']
%B5
and the next busynothing is 27104 <RequestsCookieJar[<Cookie info=%23 for .pythonchallenge.com/>]>
['27104']
%23
and the next busynothing is 54003 <RequestsCookieJar[<Cookie info=%D0 for .pythonchallenge.com/>]>
['54003']
%D0
and the next busynothing is 23501 <RequestsCookieJar[<Cookie info=%D4 for .pythonchallenge.com/>]>
['23501']
%D4
and the next busynothing is 21110 <RequestsCookieJar[<Cookie info=%D1 for .pythonchallenge.com/>]>
['21110']
%D1
and the next busynothing is 88399 <RequestsCookieJar[<Cookie info=%E2 for .pythonchallenge.com/>]>
['88399']
%E2
and the next busynothing is 49740 <RequestsCookieJar[<Cookie info=%8D for .pythonchallenge.com/>]>
['49740']
%8D
and the next busynothing is 31552 <RequestsCookieJar[<Cookie info=%06 for .pythonchallenge.com/>]>
['31552']
%06
and the next busynothing is 39998 <RequestsCookieJar[<Cookie info=%A9 for .pythonchallenge.com/>]>
['39998']
%A9
and the next busynothing is 19755 <RequestsCookieJar[<Cookie info=%FA for .pythonchallenge.com/>]>
['19755']
%FA
and the next busynothing is 64624 <RequestsCookieJar[<Cookie info=%26 for .pythonchallenge.com/>]>
['64624']
%26
and the next busynothing is 37817 <RequestsCookieJar[<Cookie info=S for .pythonchallenge.com/>]>
['37817']
S
and the next busynothing is 43427 <RequestsCookieJar[<Cookie info=%D4 for .pythonchallenge.com/>]>
['43427']
%D4
and the next busynothing is 15115 <RequestsCookieJar[<Cookie info=%D3 for .pythonchallenge.com/>]>
['15115']
%D3
and the next busynothing is 44327 <RequestsCookieJar[<Cookie info=%21 for .pythonchallenge.com/>]>
['44327']
%21
and the next busynothing is 7715 <RequestsCookieJar[<Cookie info=%A1 for .pythonchallenge.com/>]>
['7715']
%A1
and the next busynothing is 15248 <RequestsCookieJar[<Cookie info=%EA for .pythonchallenge.com/>]>
['15248']
%EA
and the next busynothing is 61895 <RequestsCookieJar[<Cookie info=i for .pythonchallenge.com/>]>
['61895']
i
and the next busynothing is 54759 <RequestsCookieJar[<Cookie info=7 for .pythonchallenge.com/>]>
['54759']
7
and the next busynothing is 54270 <RequestsCookieJar[<Cookie info=h for .pythonchallenge.com/>]>
['54270']
h
and the next busynothing is 51332 <RequestsCookieJar[<Cookie info=%9B for .pythonchallenge.com/>]>
['51332']
%9B
and the next busynothing is 63481 <RequestsCookieJar[<Cookie info=%9A for .pythonchallenge.com/>]>
['63481']
%9A
and the next busynothing is 12362 <RequestsCookieJar[<Cookie info=%2B for .pythonchallenge.com/>]>
['12362']
%2B
and the next busynothing is 94476 <RequestsCookieJar[<Cookie info=%BF for .pythonchallenge.com/>]>
['94476']
%BF
and the next busynothing is 87810 <RequestsCookieJar[<Cookie info=%60 for .pythonchallenge.com/>]>
['87810']
%60
and the next busynothing is 6027 <RequestsCookieJar[<Cookie info=%22 for .pythonchallenge.com/>]>
['6027']
%22
and the next busynothing is 47551 <RequestsCookieJar[<Cookie info=%C5 for .pythonchallenge.com/>]>
['47551']
%C5
and the next busynothing is 79498 <RequestsCookieJar[<Cookie info=W for .pythonchallenge.com/>]>
['79498']
W
and the next busynothing is 81226 <RequestsCookieJar[<Cookie info=X for .pythonchallenge.com/>]>
['81226']
X
and the next busynothing is 4256 <RequestsCookieJar[<Cookie info=%E1 for .pythonchallenge.com/>]>
['4256']
%E1
and the next busynothing is 62734 <RequestsCookieJar[<Cookie info=%AD for .pythonchallenge.com/>]>
['62734']
%AD
and the next busynothing is 25666 <RequestsCookieJar[<Cookie info=L for .pythonchallenge.com/>]>
['25666']
L
and the next busynothing is 14781 <RequestsCookieJar[<Cookie info=%80 for .pythonchallenge.com/>]>
['14781']
%80
and the next busynothing is 21412 <RequestsCookieJar[<Cookie info=%E8 for .pythonchallenge.com/>]>
['21412']
%E8
and the next busynothing is 55205 <RequestsCookieJar[<Cookie info=V for .pythonchallenge.com/>]>
['55205']
V
and the next busynothing is 65516 <RequestsCookieJar[<Cookie info=%3C for .pythonchallenge.com/>]>
['65516']
%3C
and the next busynothing is 53535 <RequestsCookieJar[<Cookie info=%C6 for .pythonchallenge.com/>]>
['53535']
%C6
and the next busynothing is 4437 <RequestsCookieJar[<Cookie info=%A8 for .pythonchallenge.com/>]>
['4437']
%A8
and the next busynothing is 43442 <RequestsCookieJar[<Cookie info=%DB for .pythonchallenge.com/>]>
['43442']
%DB
and the next busynothing is 91308 <RequestsCookieJar[<Cookie info=H for .pythonchallenge.com/>]>
['91308']
H
and the next busynothing is 1312 <RequestsCookieJar[<Cookie info=%26 for .pythonchallenge.com/>]>
['1312']
%26
and the next busynothing is 36268 <RequestsCookieJar[<Cookie info=3 for .pythonchallenge.com/>]>
['36268']
3
and the next busynothing is 34289 <RequestsCookieJar[<Cookie info=2 for .pythonchallenge.com/>]>
['34289']
2
and the next busynothing is 46384 <RequestsCookieJar[<Cookie info=%18 for .pythonchallenge.com/>]>
['46384']
%18
and the next busynothing is 18097 <RequestsCookieJar[<Cookie info=%A8 for .pythonchallenge.com/>]>
['18097']
%A8
and the next busynothing is 9401 <RequestsCookieJar[<Cookie info=x for .pythonchallenge.com/>]>
['9401']
x
and the next busynothing is 54249 <RequestsCookieJar[<Cookie info=%01 for .pythonchallenge.com/>]>
['54249']
%01
and the next busynothing is 29247 <RequestsCookieJar[<Cookie info=%08 for .pythonchallenge.com/>]>
['29247']
%08
and the next busynothing is 13115 <RequestsCookieJar[<Cookie info=%21 for .pythonchallenge.com/>]>
['13115']
%21
and the next busynothing is 23053 <RequestsCookieJar[<Cookie info=%8D for .pythonchallenge.com/>]>
['23053']
%8D
and the next busynothing is 3875 <RequestsCookieJar[<Cookie info=S for .pythonchallenge.com/>]>
['3875']
S
and the next busynothing is 16044 <RequestsCookieJar[<Cookie info=%0B for .pythonchallenge.com/>]>
['16044']
%0B
and the next busynothing is 8022 <RequestsCookieJar[<Cookie info=%C8 for .pythonchallenge.com/>]>
['8022']
%C8
and the next busynothing is 25357 <RequestsCookieJar[<Cookie info=%AF for .pythonchallenge.com/>]>
['25357']
%AF
and the next busynothing is 89879 <RequestsCookieJar[<Cookie info=%96 for .pythonchallenge.com/>]>
['89879']
%96
and the next busynothing is 80119 <RequestsCookieJar[<Cookie info=K for .pythonchallenge.com/>]>
['80119']
K
and the next busynothing is 50290 <RequestsCookieJar[<Cookie info=O for .pythonchallenge.com/>]>
['50290']
O
and the next busynothing is 9297 <RequestsCookieJar[<Cookie info=%CA for .pythonchallenge.com/>]>
['9297']
%CA
and the next busynothing is 30571 <RequestsCookieJar[<Cookie info=2 for .pythonchallenge.com/>]>
['30571']
2
and the next busynothing is 7414 <RequestsCookieJar[<Cookie info=%B0 for .pythonchallenge.com/>]>
['7414']
%B0
and the next busynothing is 30978 <RequestsCookieJar[<Cookie info=%F1 for .pythonchallenge.com/>]>
['30978']
%F1
and the next busynothing is 16408 <RequestsCookieJar[<Cookie info=%BD for .pythonchallenge.com/>]>
['16408']
%BD
and the next busynothing is 80109 <RequestsCookieJar[<Cookie info=%1D for .pythonchallenge.com/>]>
['80109']
%1D
and the next busynothing is 55736 <RequestsCookieJar[<Cookie info=u for .pythonchallenge.com/>]>
['55736']
u
and the next busynothing is 15357 <RequestsCookieJar[<Cookie info=%A0 for .pythonchallenge.com/>]>
['15357']
%A0
and the next busynothing is 80887 <RequestsCookieJar[<Cookie info=%86 for .pythonchallenge.com/>]>
['80887']
%86
and the next busynothing is 35014 <RequestsCookieJar[<Cookie info=%05 for .pythonchallenge.com/>]>
['35014']
%05
and the next busynothing is 16523 <RequestsCookieJar[<Cookie info=%92 for .pythonchallenge.com/>]>
['16523']
%92
and the next busynothing is 50286 <RequestsCookieJar[<Cookie info=s for .pythonchallenge.com/>]>
['50286']
s
and the next busynothing is 34813 <RequestsCookieJar[<Cookie info=%B0 for .pythonchallenge.com/>]>
['34813']
%B0
and the next busynothing is 77562 <RequestsCookieJar[<Cookie info=%92 for .pythonchallenge.com/>]>
['77562']
%92
and the next busynothing is 54746 <RequestsCookieJar[<Cookie info=%C4 for .pythonchallenge.com/>]>
['54746']
%C4
and the next busynothing is 22680 <RequestsCookieJar[<Cookie info=B for .pythonchallenge.com/>]>
['22680']
B
and the next busynothing is 19705 <RequestsCookieJar[<Cookie info=c for .pythonchallenge.com/>]>
['19705']
c
and the next busynothing is 77000 <RequestsCookieJar[<Cookie info=%F1 for .pythonchallenge.com/>]>
['77000']
%F1
and the next busynothing is 27634 <RequestsCookieJar[<Cookie info=w for .pythonchallenge.com/>]>
['27634']
w
and the next busynothing is 21008 <RequestsCookieJar[<Cookie info=%24 for .pythonchallenge.com/>]>
['21008']
%24
and the next busynothing is 64994 <RequestsCookieJar[<Cookie info=S for .pythonchallenge.com/>]>
['64994']
S
and the next busynothing is 66109 <RequestsCookieJar[<Cookie info=%85 for .pythonchallenge.com/>]>
['66109']
%85
and the next busynothing is 37855 <RequestsCookieJar[<Cookie info=%09 for .pythonchallenge.com/>]>
['37855']
%09
and the next busynothing is 36383 <RequestsCookieJar[<Cookie info=%09 for .pythonchallenge.com/>]>
['36383']
%09
and the next busynothing is 68548 <RequestsCookieJar[<Cookie info=C for .pythonchallenge.com/>]>
['68548']
C
and the next busynothing is 96070 <RequestsCookieJar[<Cookie info=%AE for .pythonchallenge.com/>]>
['96070']
%AE
and the next busynothing is 83051 <RequestsCookieJar[<Cookie info=%24 for .pythonchallenge.com/>]>
['83051']
%24
that's it. <RequestsCookieJar[<Cookie info=%90 for .pythonchallenge.com/>]>
[]


 ['B', 'Z', 'h', '9', '1', 'A', 'Y', '%26', 'S', 'Y', '%94', '%3A', '%E2', 
 'I', '%00', '%00', '%21', '%19', '%80', 'P', '%81', '%11', '%00', '%AF', 
 'g', '%9E', '%A0', '+', '%00', 'h', 'E', '%3D', 'M', '%B5', '%23', '%D0', 
 '%D4', '%D1', '%E2', '%8D', '%06', '%A9', '%FA', '%26', 'S', '%D4', '%D3', 
 '%21', '%A1', '%EA', 'i', '7', 'h', '%9B', '%9A', '%2B', '%BF', '%60', '%22', 
 '%C5', 'W', 'X', '%E1', '%AD', 'L', '%80', '%E8', 'V', '%3C', '%C6', '%A8', '%DB', 
 'H', '%26', '3', '2', '%18', '%A8', 'x', '%01', '%08', '%21', '%8D', 'S', '%0B', '%C8', 
 '%AF', '%96', 'K', 'O', '%CA', '2', '%B0', '%F1', '%BD', '%1D', 'u', '%A0', '%86', '%05', 
 '%92', 's', '%B0', '%92', '%C4', 'B', 'c', '%F1', 'w', '%24', 'S', '%85', '%09', '%09', 'C', '%AE', '%24']
[Finished in 109.8s]
'''

# 把cookies合并得到
'''
BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4
%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C
%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s
%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24
[Finished in 0.4s]
'''

# 转码得到
'''
b'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#
\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1
\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0
\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$'
'''

# 上面结果有误，重新调整边界条件得到
'''
b'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#
\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1
\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0
\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$\x90'
b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'
[Finished in 88.3s]
'''