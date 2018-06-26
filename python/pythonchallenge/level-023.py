#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-06-26 15:20:13
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 23 of python challenge
# 
# 思路：这一关的网页上同样是一张图，图片上显示了一头在公路旁吃草牛，然后就没有其他线索了，打开源码这一关显示了很多信息
#       首先是最上方的一段话
#       <!--
#       TODO: do you owe someone an apology? now it is a good time to
#       tell him that you are sorry. Please show good manners although
#       it has nothing to do with this level.
#       -->
#       提起道歉的事情，好像是前几关，大概是19、20关的时候，网址为http://www.pythonchallenge.com/pc/hex/idiot.html
#       页面上提到了Now you should apologize...，图片上显示了一个人，我不知道他叫什么名字，但是图片名字显示为stuff/leopold.jpg
#       
#       接下来的线索是标题：what is this module? 貌似是让我猜出模块的名字，这一关应该是用了一个新模块
#       然后还有提示信息<!--    it can't find it. this is an undocumented module. --> 提示说这个模块是非正式的，难道是野模块？
#       
#       最后的提示信息为:
#       <!--
#       'va gur snpr bs jung?'
#       -->
#       我完全看不懂这个提示，但是有道词典居然翻译成 你是谁？另我感到有点吃惊，
#       
#       综上所述，我感觉可能是调用某个远程方法给leopold道歉，然后会得到一些关于这个非正式模块的信息，试试吧
#       仔细想想可能不需要道歉，因为...although it has nothing to do with this level.
#       
#       再一次没有自己做出来，我已经习惯了，果然和道歉没有什么关系，但是和标题有关系what is this module这句话的重点是this
#       原来python真的有个模块叫this，导入之后发现了一段话，原来是Python的哲学：
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
#       
#       仔细理解一下，原来this is an undocumented module.这句话中的this也是带引号的，然后线索还有最后一句话
#       va gur snpr bs jung?，貌似是通过偏移得到的，采用第一关的方法尝试一下：
#       其中只有一句看得出含义in the face of what?，这句话在import之后出现过类似的，那就是In the face of ambiguity,
#       至此我们就发现了通向下一关的url，那就是ambiguity.html
#       
#       
#       
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/hex/bonus.html
#       3. next level url : http://www.pythonchallenge.com/pc/hex/ambiguity.html
#       4. curlevel username:butter password:fly
#

import string
import this

def auto_trans(src_str):
    for x in range(26):
        trans_table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'[x:x+26])
        print(src_str.translate(trans_table))

def main():
    auto_trans('va gur snpr bs jung?')


if __name__ == '__main__':
    main()

# 输出信息
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
va gur snpr bs jung?
wb hvs toqs ct kvoh?
xc iwt uprt du lwpi?
yd jxu vqsu ev mxqj?
ze kyv wrtv fw nyrk?
af lzw xsuw gx ozsl?
bg max ytvx hy patm?
ch nby zuwy iz qbun?
di ocz avxz ja rcvo?
ej pda bwya kb sdwp?
fk qeb cxzb lc texq?
gl rfc dyac md ufyr?
hm sgd ezbd ne vgzs?
in the face of what?
jo uif gbdf pg xibu?
kp vjg hceg qh yjcv?
lq wkh idfh ri zkdw?
mr xli jegi sj alex?
ns ymj kfhj tk bmfy?
ot znk lgik ul cngz?
pu aol mhjl vm doha?
qv bpm nikm wn epib?
rw cqn ojln xo fqjc?
sx dro pkmo yp grkd?
ty esp qlnp zq hsle?
uz ftq rmoq ar itmf?
[Finished in 0.2s]
'''