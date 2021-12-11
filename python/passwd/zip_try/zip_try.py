#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# try a passwd for zip file

import time
from typing import List
from tqdm import tqdm
from itertools import chain
from zipfile import ZipFile
import subprocess
import pyzipper

ts = time.time()
def gen_dict():
    # chr(97) -> 'a' 这个变量保存了密码包含的字符集
    dictionaries = [chr(i) for i in
                    chain(range(97, 123),    # a - z
                          range(65, 91),    # A - Z
                          range(48, 58))]    # 0 - 9

    # 添加自定义的字符集
    dictionaries.insert(0, 'www.')
    dictionaries.extend(['.com', '!', '@', '#', '$', '%', '^', '&', '*', '-', '=', '+'])
    print(len(dictionaries))
    return dictionaries

def all_passwd(dictionaries: List[str], maxlen: int):
    # 返回由 dictionaries 中字符组成的所有长度为 maxlen 的字符串

    def helper(temp: list, start: int, n: int):
        # 辅助函数，是个生成器
        if start == n:    # 达到递归出口
            yield ''.join(temp)
            return
        for t in dictionaries:
            temp[start] = t    # 在每个位置
            yield from helper(temp, start + 1, n)

    yield from helper([0] * maxlen, 0, maxlen)

def extract(zfile: ZipFile, pwd: str) -> bool:
    # zfile: 一个ZipFile类, pwd: 密码
    global ts
    if time.time() - ts > 10 :
        ts = time.time()
        print(pwd)

    try:
        zfile.extractall(path='.', pwd=pwd.encode('utf-8'))    # 密码输入错误的时候会报错
        now = time.time()                                      # 故使用 try - except 语句
        print(f"Password is: {pwd}")                           # 将正确的密码输出到控制台
        return True
    except:
        return False

def extract2(file_name: str, pwd: str) -> bool:
    global ts
    if time.time() - ts > 10 :
        ts = time.time()
        print(pwd)

    command='D:/NoBlankProgram/7-Zip/7z.exe -P'+ pwd + ' t ' + file_name
    ret = subprocess.call(command)
    #os.popen(command)#这个也可以用,但是不好监控解压状态
    #print(child)
    if ret == 0:
        print(f"Password is: {pwd}")                           # 将正确的密码输出到控制台
        return True
    else:
        return False

def extract3(f, pwd) -> bool:
    global ts
    if time.time() - ts > 10 :
        ts = time.time()
        print(pwd)

    f.pwd = pwd.encode('utf-8')
    try:
        f.extractall()                  # 密码输入错误的时候会报错
        print(f"Password is: {pwd}")    # 将正确的密码输出到控制台
        return True
    except:
        return False

def main(file_name):
    start = time.time()
    zfile = ZipFile(file_name, 'r')    # 很像open
    pyz = pyzipper.AESZipFile(file_name,'r')

    dictionaries = gen_dict()
    print(dictionaries)

    lengths = [5]    # 密码长度
    total = sum(len(dictionaries) ** k for k in lengths)    # 密码总数

    for pwd in tqdm(chain.from_iterable(all_passwd(dictionaries, maxlen) for maxlen in lengths), total=total):
        #if extract(zfile, pwd):    # 记得extract函数返回的是bool类型的哦
        #if extract2(file_name, pwd):
        if extract3(pyz, pwd):
            break

if __name__ == "__main__":
    main('F:\\movie\\tangtan3.zip')
    #print(ts)
    #zfile = ZipFile('./abq.zip', 'r')
    #zfile.extractall(path='.', pwd='fuck'.encode('utf-8'))
    #print(extract(ZipFile('abq.zip', 'r'), 'fuck'))