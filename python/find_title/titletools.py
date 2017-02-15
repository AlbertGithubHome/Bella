#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# crawler title for little lightning
import urllib.request, re

# configuration
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'
}

re_template = r'(?<=target="_blank">)(.+?)(?=</a> </li>)'
target_url = "http://www.gov.cn/guowuyuan/zuzhi.htm"


# main logic
def crawler_html():
    req = urllib.request.Request(url = target_url, headers = req_headers)
    res = urllib.request.urlopen(req)
    data = res.read()

    result = re.findall(re_template, data.decode('utf-8'))
    #print(result)
    for item in result:
        item = item.replace(' ', '')
        print(item)

# start to crawler
if __name__ == '__main__':
    print("little lightning tools running...\n")
    crawler_html()
