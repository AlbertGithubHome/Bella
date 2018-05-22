#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-22 13:39:51
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 13 of python challenge
# 
# 思路：打开这一关只看到一个画着电话的图片，并且图片下方有一个提示phone that evil，标题的内容是call him
#       根据提示就是给evil打电话喽，然后没有发现其他线索，于是打开源码发现一个隐藏的链接，地址为
#       http://www.pythonchallenge.com/pc/phonebook.php，点击后发现返回一个xml格式的内容，好像是提示错误
#       内容为：faultCode 105 faultString XML error: Invalid document end at line 1, column 1，具体格式参考代码后内容
#       进行到这一步实在没有头绪了，网上搜索需要使用Python下的XML-RPC，rpc也就是远程过程调用， 一般使用在客户端使用xmlrpclib，
#       可以用来调用注册在XML-RPC服务器端的函数，依照使用代码先创建服务器，然后调用phone函数给evil打电话，
#       evil的名字在12关已经给出，也就是需要给Bert打电话，将返回值打印就得到了结果555-ITALY，也就是555时号码喽，看代码时，
#       图片中电话机5的位置正好是触发链接的位置，ITALY就是下一关的url
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/disproportional.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/italy.html
#       4. username:huge password:file
#

import xmlrpc.client

# image url
target_url = 'http://www.pythonchallenge.com/pc/phonebook.php'

def list_functions(server):
    print(server.system.listMethods())
    print(server.system.methodHelp('phone'))

def main():
    server = xmlrpc.client.ServerProxy(target_url)
    print(server.phone('Bert'))
    list_functions(server)

if __name__ == '__main__':
    main()


# http://www.pythonchallenge.com/pc/phonebook.php返回的xml内容
'''
<?xml version="1.0"?>
<methodResponse>
<fault>
<value>
<struct><member><name>faultCode</name>
<value><int>105</int></value>
</member>
<member>
<name>faultString</name>
<value><string>XML error: Invalid document end at line 1, column 1</string></value>
</member>
</struct>
</value>
</fault>
</methodResponse>
'''
# 运行结果，以及服务端可以调用的函数
'''
555-ITALY
['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
Returns the phone of a person
[Finished in 1.2s]
'''
