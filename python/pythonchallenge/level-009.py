#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-08 13:37:23
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 9 of python challenge
# 
# 思路：这一关的线索是图片上的小黑点，想把他们连起来，可是没有办法知道点的坐标，于是打开源码看看
#       发现这一关的线索给了两个数字序列，还提示要加起来，可是first序列和second序列在数量上跟本不相等
#       于是还是参考一下大家的想法，使用Image来画图吧，后来发现还需要使用ImageDraw库，将first序列和second序列
#       作为线上的点直接传给函数作为参数就可以，注意还要有原图的大小。序列与图片大小都可以通过网页源码获得
#       但是这个网页是需要认证的，尝试认证这个网页花费了不少时间，requests,session,cookies,post,get都是过了也不行
#       后来发现urllib.request可以做到，参考下面的test函数，紧接着发现requests也可以，并且更简单，于是又改成了requests
#       然后利用正则表达式获得图片长和宽，还有first和second序列，具体代码在函数get_html_content()中
#       接着通过Image创建图片，通过ImageDraw画图片，然后展示出来是一头牛，那么下一关的url应该就是bull，我很疑惑
#       为什么不是cow
#       
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/good.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/bull.html
#       4. username:huge password:file


from PIL import ImageDraw,Image
import requests
import re

# level url
target_url = 'http://www.pythonchallenge.com/pc/return/good.html'

def get_html_content():
    login_data = requests.get(target_url, auth=('huge', 'file')).content
    content = login_data.decode('utf-8')
    width = int(re.findall(r'width=\"(\d+)', content)[0]);
    height = int(re.findall(r'height=\"(\d+)', content)[0]);
    #print(content)
    content = content.replace('\n', '');
    first_content = re.findall(r'first:(.+)second', content)[0];
    second_content = re.findall(r'second:(.+)-->', content)[0];
    print(width, height)
    print(first_content);
    print(second_content);
    return width, height, list(map(int, first_content.split(","))), list(map(int, second_content.split(",")))


def main():
    width, height, first_list, second_list =get_html_content()
    #print(width, height, first_list, second_list)
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    draw.line(first_list)
    draw.line(second_list)
    img.show()


if __name__ == '__main__':
    main()

# 一种通过账号密码直接登录验证网站的方式
# 后来发现可以通过 requests.get(target_url, auth=('huge', 'file')) 实现
import urllib.request
def test():
    # create a password manager  
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
      
    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    top_level_url = "http://www.pythonchallenge.com/pc/return/good.html"
    password_mgr.add_password(None, top_level_url, 'huge', 'file')
      
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
      
    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    a_url = "http://www.pythonchallenge.com/pc/return/good.html"
    x = opener.open(a_url)
    print(x.read())
      
    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    urllib.request.install_opener(opener)
    a = urllib.request.urlopen(a_url).read().decode('utf8')
    print(a) 


# 解析网页结果，没有回车，为了显示自己加的
'''
640 480
146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,
320,170,310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,
191,312,190,316,190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,
380,197,383,196,387,192,389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,
219,397,219,393,216,390,215,385,215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,
329,214,319,215,311,215,306,216,296,218,290,221,283,225,282,233,284,238,287,243,290,250,291,
255,294,261,293,265,291,271,291,273,289,278,287,279,285,281,280,284,278,284,276,287,277,289,
283,291,286,294,291,296,295,299,300,301,304,304,320,305,327,306,332,307,341,306,349,303,354,
301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,328,375,329,367,329,353,330,
341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,259,346,251,349,259,
349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,352,257,351,
249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,120,
314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,
137,214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,
176,114,176,102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,
115,120,115,115,117,113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,
93,129,100,130,108,132,110,133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,
165,97,167,99,171,109,171,107,161,111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,
259,136,266,139,276,143,290,148,310,151,332,155,348,156,353,153,366,149,379,147,394,146,399
156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,
159,157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,
132,220,125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,
164,81,162,77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,
114,155,115,158,121,157,128,156,134,157,136,156,136
[Finished in 0.8s]
'''

