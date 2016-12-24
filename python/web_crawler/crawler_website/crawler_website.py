#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# crawler picture with pretending browser
import urllib.request, socket, re, sys, os

# save file path
target_path = ".\\crawler_article_set"
target_url = "http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'
}

def crawler_html(url_path):
    
    req = urllib.request.Request(url = url_path, headers = req_headers)
    res = urllib.request.urlopen(req)
    data = res.read()

    title = list(re.findall(r'(?<=<h4>).+?(?=</h4>)', str(data)))[0]
    print(title)

    #L = list(map(ord, title))
    #print(L)
    title = bytearray(title, 'utf-8')
    print(title)
    #ret = b''
    #ret = ret + list[1]
    #print(ret)


    print("==========", title.decode('utf-8'))

    '中文'.encode('utf-8')
    print('中文'.encode('utf-8'))

    print(b'\xe5\xae\x9a\xe4\xb9\x89\xe5\x87\xbd\xe6\x95\xb0'.decode('utf-8'))


    #with open(str(title), 'w') as file:
        #file.write(data)

def start_crawler():
    #create dir if not exist
    if not os.path.isdir(target_path):
        os.mkdir(target_path)

    req = urllib.request.Request(url = target_url, headers = req_headers)
    res = urllib.request.urlopen(req)
    data = res.read()

    url_set = set(re.findall(r'(wiki/[\S]*(?="))', str(data)))
    url_list = list(map(lambda x : 'http://www.liaoxuefeng.com/' + x, url_set))

    all_url = '\n'.join(url_list)
    #print(all_url)
    print(len(url_set))

    with open('www.liaoxuefeng.com.txt', 'w') as file:
        file.write(all_url)

    print(url_list[0])
    crawler_html(url_list[0])

# start to crawler
if __name__ == '__main__':
    start_crawler()