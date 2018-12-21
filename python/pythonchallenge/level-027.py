#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-12-18 16:08:35
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 28 of python challenge
# 
# 思路：网页上一张图显示了一幅风景画，图上显示是在水面上，应该是在船上，画面上青山绿水，最引人注目的是一个船桨，
#       好像一个画笔一样，空中有笔画过的痕迹，看起来像M、N或者W，形如NW，还不知道具体什么含义，打开源码发现，
#       标题为between the tables，难道谜底在两个表或者桌子之间？
#       
#       图片链接了一个网址"../ring/bell.html"，点击之后无法打开，需要用户名和密码，目前还没有找到，图片的名字为
#       "zigzag.jpg"，并且后面还有注释内容<!-- did you say gif? -->，原本是jpg，看完提示改为gif果然打开了另一幅图，
#       这是一幅只有黑白像素点的图，画面上应该看不出来什么线索，具体的思路应该在处理图片数据上，源码最后给了一句提示
#       <!-- oh, and this is NOT a repeat of 14 -->用来说明这关与14关不同
#       
#       14关的地址为http://www.pythonchallenge.com/pc/return/italy.html，图片是一个面包圈，一圈圈向里，
#       所以把图片数据一圈圈向里得到了最终的结果，这一关已经给出提示不能那样做？不知道是不是真的
#       
#       zigzag的意思是曲折的，好像是图片的上的那个折来折去，哎，既然和14关的转圈圈不一样，那会不会是相似呢？
#       可能是折来折去的，先试试
#       
#       还没尝试，据说不行，还要用到调色板，先看看调色板知识吧，GIF图像格式参考一下网址：
#       http://www.cnblogs.com/think/archive/2006/04/12/372942.html，介绍的非常详细，当然很多信息都被python封装好了
#       比如调色板，可以直接调用img.getpalette()
#       
#       使用调色板替换原数据，打印各自的前一部分发现，差了一个字节，对齐后逐次比较不同，在不同的像素点输出灰度图像，
#       最后得到一幅图片，上面写着not word，另一份把原数据中不同的位置的字节拼到一起是一个BZ2压缩文件，解压后得到
#       一些单词，结合前面的not word，把python关键字都去掉，剩余../ring/bell.html、switch、repeat、exec、print，
#       在把exec和print两个函数去掉，尝试后得知bell就是下一关的网址，switch和repeat分别是账号和密码
#       
#       
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/hex/speedboat.html
#       3. next level url : http://www.pythonchallenge.com/pc/ring/bell.html
#       4. curlevel username:butter password:fly
#

from PIL import Image
import requests
import bz2
import keyword

# image url
target_url = 'http://www.pythonchallenge.com/pc/hex/zigzag.gif'

def download_image():
    image_data = requests.get(target_url, auth=('butter', 'fly')).content
    with open("challenge27/zigzag.gif", "wb") as file:
        file.write(image_data)

def read_lolcal_image():
    with open("challenge27/zigzag.gif", "rb") as file:
        return file.read()

def handle_image():
    img = Image.open("challenge27/zigzag.gif")
    img_date = img.tobytes()
    #print(type(img_date))
    #print(type(img_date[0]))
    #print(type(img_date[0:1]))

    palette = img.getpalette()
    pixel_list = palette[::3] #RGB value is the same
    #print(palette)
    #print(pixel_list)

    trans_table = bytearray.maketrans(bytes([i for i in range(256)]), bytes(pixel_list))
    trans_data = img_date.translate(trans_table);

    print(img_date[:10])
    print(trans_data[:10])

    diff = [b'',b'']
    new_img = Image.new('1', img.size, 0)
    for i in range(1, len(img_date)):
        if img_date[i]!=trans_data[i-1]:
            diff[0] += img_date[i:i+1]  # chr(img_date[i]).encode() # img_date[i].to_bytes(1, byteorder = 'little')
            new_img.putpixel(((i-1)%img.size[0], (i-1)//img.size[0]),1)
    new_img.save('challenge27/27.png')
    text = bz2.decompress(diff[0])
    #print(text);
    for i in str(text,'utf-8').split():
        if not keyword.iskeyword(i):
            print(i)


def main():
    img_data = read_lolcal_image()
    print(img_data[:10])
    print(eval("3+7"))
    handle_image()
    t = 1
    #print(t.to_bytes(1, byteorder = 'little'))
    #print(chr(49).encode())
    #print(bytes([49]))
    #print(bytes([49]) == chr(49).encode())
    #print(str(b'abc','utf-8'))

if __name__ == '__main__': main()


# 直接将图片字节转换成Image报错
'''
Traceback (most recent call last):
  File "E:\GitProject\Bella\python\pythonchallenge\level-027.py", line 65, in <module>
    if __name__ == '__main__': get_image()
  File "E:\GitProject\Bella\python\pythonchallenge\level-027.py", line 43, in get_image
    img = Image.open(stream)
  File "D:\Program Files\Python36\lib\site-packages\PIL\Image.py", line 2657, in open
    % (filename if filename else fp))
OSError: cannot identify image file <_io.BytesIO object at 0x000001AF3D60F7D8>
[Finished in 1.5s]
'''
# 通过打印前一部分发现，差了一个字节
'''
print(img_date[:10])
print(trans_data[:10])

b'\xd7\xd0\xcb\x0c\xfe<\x8bHB\xbd'
b'\xd0\xcb\x0c\xfe<\x8bHB\xbd\x7f'

'''

# 不同的字节解压后打印
'''
b'../ring/bell.html del assert repeat raise or class is exec return except print return switch 
from exec repeat else not while assert or class class break except assert yield finally 
../ring/bell.html assert ../ring/bell.html in is yield and import break def ../ring/bell.html global 
repeat if yield pass exec del return def or repeat switch for else or break if global def raise lambda 
and else for ../ring/bell.html pass ../ring/bell.html elif break else is except if class import assert 
is lambda continue not finally global finally lambda class exec pass yield and break is assert elif def 
while break elif global assert except if import pass from for repeat global raise exec finally yield 
lambda class from or and break not try elif or finally yield if is raise except print lambda elif finally 
is if ../ring/bell.html is while global finally return while def continue in except assert and class assert 
global return finally import print import and del while raise elif print pass try switch import try try 
assert while return is in if continue try in from repeat global repeat in or not from if exec try del 
pass return except pass assert switch or assert ../ring/bell.html print continue try raise is for continue 
lambda else for in and yield from and pass elif break finally continue from elif while or except in or print 
global elif while def yield in def return lambda del finally not for ../ring/bell.html or try or from except 
finally def pass exec print class break return not import except or break import break global in from import 
return repeat pass yield break yield not for yield except yield in print yield class class ../ring/bell.html 
repeat repeat except def lambda class try def for global ../ring/bell.html and else ../ring/bell.html in print 
in global continue elif raise or is in yield is finally global from lambda global if finally from for not 
raise def not assert lambda return exec import yield from print not while del elif is elif except while not 
global try and global is exec ../ring/bell.html or assert break def print for raise assert not continue and 
in exec from exec for ../ring/bell.html for del try break while class assert return is for print is pass from 
break import from finally global repeat or import not elif class switch print class for while exec assert global 
elif switch def lambda elif and repeat continue global exec switch finally except break or from continue del pass 
return while assert lambda from finally while pass lambda try break lambda finally while except break yield and 
raise finally try is ../ring/bell.html else yield finally exec repeat not break elif elif break while try raise 
def continue while try assert for ../ring/bell.html exec pass yield in return or if import print assert global 
switch print for raise switch for from del def in not try in repeat and elif in yield return assert return repeat 
assert def try print while repeat from not in repeat lambda pass switch global not while except for not repeat 
assert class and not class repeat try assert raise is global def del or repeat from finally yield assert for or 
except return in ../ring/bell.html if and exec ../ring/bell.html break def raise and break raise raise def is def 
else break repeat or import del assert assert assert assert elif global except raise except continue yield elif 
def or switch raise finally elif break raise pass continue def elif def raise del global repeat and def else 
finally switch pass assert continue lambda in is is while try lambda or or while not else from in continue while 
finally and repeat raise lambda ../ring/bell.html for or finally switch try finally def for raise del global print 
finally elif if if try continue while def print for finally in not global is lambda return return yield assert lambda 
def exec repeat try repeat continue yield except lambda except def else in yield and return else yield switch from del 
not is raise if in print class exec raise class if is def for switch continue pass from except is return ../ring/bell.html 
yield return def pass yield from try except except import finally try assert lambda break try yield except global 
raise assert global try except assert exec elif break ../ring/bell.html import finally finally except assert from and 
continue exec else assert not print else ../ring/bell.html not ../ring/bell.html break if finally assert ../ring/bell.html 
except assert finally break pass print and lambda if lambda is except not if except exec lambda for ../ring/bell.html 
del if not global yield repeat global for break del or import ../ring/bell.html continue from break in is 
repeat switch global repeat repeat continue import print import assert yield break lambda if is lambda ../ring/bell.html 
finally raise except and break not pass del exec lambda for del ../ring/bell.html ../ring/bell.html if for return try 
for return is assert while while class finally while from elif try elif is global break while return class try import switch 
else and yield or return exec break or return repeat raise in while yield from return is class del for for not continue 
if finally elif else from while or continue continue in except break class is del import and def while exec finally lambda 
import global and and in and is ../ring/bell.html or yield and global try while in def try finally is del raise while from 
elif ../ring/bell.html and exec yield global def exec try import while from or continue for if lambda return or yield from 
while class finally or finally class yield continue try is except from or if elif while print continue raise try yield from 
try is break print exec def global del not exec continue return def if switch in global switch and def else switch assert 
elif continue or switch switch continue finally try pass finally ../ring/bell.html def break and try yield or lambda else 
return raise return else lambda import pass print else break yield ../ring/bell.html def lambda and class except or lambda 
print from not except elif raise pass from and del exec repeat try raise def not not class not return or break except elif 
return not class class switch print lambda break global for switch switch or else try from import in ../ring/bell.html from 
pass class except print switch is in for def raise if pass del print yield break return print elif else lambda repeat if elif 
def import break lambda if lambda in for not ../ring/bell.html from try lambda except exec repeat try is continue else exec 
while elif finally not switch else elif print def yield else raise break elif assert from for not exec not yield repeat 
continue else yield try try in is and return break and yield import lambda raise return and not assert del ../ring/bell.html 
and from or global and del break for repeat elif pass finally is in assert if lambda finally yield pass except in or continue 
from assert break from or if continue pass import finally ../ring/bell.html for del or pass return switch or not continue assert 
...
后面部分省略
...
'''
