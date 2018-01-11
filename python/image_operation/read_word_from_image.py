#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import os
import urllib.parse
import webbrowser
import requests
import base64
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# 需要在 https://cloud.baidu.com/product/ocr 上注册新建应用
# 调用百度OCR API，每天有次数限制, 这里需要换成你自己注册的
api_key = 'uHIDkc8lR9CQ00t4GuGuateLu'
api_secret = 'vVxFZkqdi200YlwucafU4Eszdc5h0MpFp'

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')

# 展示题目图片
def show_question_image(region):
    plt.imshow(region, animated=True)
    plt.show()

# 获取题目图片
def get_question_image():
    pull_screenshot()
    img = Image.open("./screenshot.png")
    #region = img.crop((50, 350, 1000, 560)) # 1920 x 1080
    region = img.crop((50, 350, 1000, 560)) # 1920 x 1080

    # 查看图片
    show_question_image(region)
    
    # 利用切割数据成像
    img_bytes = io.BytesIO()
    region.save(img_bytes, format='PNG')
    return imgByteArr.getvalue()

def get_baidu_token():
    res = requests.get(url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+ api_key + '&client_secret=' + api_secret,
        headers={ 'Content-Type':'application/json;charset=UTF-8' }).json()
    return res['access_token']

def get_image_words(token, base64_data):
    content = requests.post('https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
              params={'access_token': token}, data={'image': base64_data})

    result = ''
    for i in content.json()['words_result']:
        result += i['words']
    return urllib.parse.quote(result)

def main():
    base64_data = base64.b64encode(get_question_image())
    #token = get_baidu_token(token, base64_data)
    #images_words = get_image_words()
    #print("images_words=" + images_words)
    #webbrowser.open('https://baidu.com/s?wd='+ images_words)

if __name__ == '__main__':
    main()
