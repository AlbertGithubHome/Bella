#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# crawler picture with pretending browser
import urllib.request, socket, re, sys, os
from io import BytesIO

# save file path
target_path = ".\\crawler_article_set"
target_url = "http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'
}

def test_encode():
    #print(title)
    '''
    print(type(title))
    t =bytes(map(ord, title))
    print(len(t))
    print(t)
    print(type(title))

    print()
    s = '\xe5\x88\x86\xe5\xb8\x83\xe5\xbc\x8f\xe8\xbf\x9b\xe7\xa8\x8b'
    print(type(s))
    b = bytes(map(ord, s))
    print(len(b))
    print(b)
    print(type(s))
    '''

    '''
    print(len(title))
    b =  bytes(title, encoding='ascii')
    print(b)
    print(len(b))
    ret = b.decode('utf-8')
    print(ret)
    '''
    #AAA = eval(title)
    #print()
    #new_title = 'b\''+ title + '\''
    #print('title =', new_title)
    #type(new_title)
    #f = BytesIO(new_title)

    #L = list(map(ord, title))
    #print(L)
    #title = bytearray(title, 'utf-8')
    #print(title)
    #ret = b''
    #ret = ret + list[1]
    #print(ret)
    #f = BytesIO(b'')
    #f.append(titile)
    #print(f.read())
    #
    '''
    BBBB = b'\xe4\xb8\xad\xe6\x96\x87';
    print('BBBB =', BBBB)
    print('str(BBBB) =', 'ac' + str(BBBB))
    '''


    #print("==========", title.decode('utf-8'))
    '''
    '中文'.encode('utf-8')
    print('中文'.encode('utf-8'))

    print(b'\xe5\xae\x9a\xe4\xb9\x89\xe5\x87\xbd\xe6\x95\xb0'.decode('utf-8'))

    print(re.findall(r'函数', b'\xe5\xae\x9a\xe4\xb9\x89\xe5\x87\xbd\xe6\x95\xb0'.decode('utf-8')))
    '''

def crawler_html(url_path):
    
    req = urllib.request.Request(url = url_path, headers = req_headers)
    res = urllib.request.urlopen(req)
    data = res.read()

    title = list(re.findall(r'(?<=<h4>).+?(?=</h4>)', data.decode('utf-8')))[0]
    # test encode and decode a long time
    test_encode()

    title = title.replace('/', '_')
    with open(os.path.join('crawler_article_set', title) + '.html', 'wb') as file:
        file.write(data)


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
    print('total article count =', len(url_set))

    with open('www.liaoxuefeng.com_python.txt', 'w') as file:
        file.write(all_url)

    count = 0
    for url in url_list:
        crawler_html(url)
        print(url)
        count = count + 1
        print('finish article :', count)

# start to crawler
if __name__ == '__main__':
    start_crawler()
