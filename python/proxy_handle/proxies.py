#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-18 15:18:28
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 学习网络代理的使用，提供获取代理地址的的方法

import requests
import random
import re

#regex_ip_port_src = '<td data-title="IP">183.148.135.58</td>das<td data-title="PORT">9999</td>'
#regex_ip_port = r'<td data-title="IP">([.0-9]+?)</td>.*?<td data-title="PORT">(\d+)</td>'
#print(re.findall(r'^ddasfasdfjaskdf(\d)', 'ddasfasdfjaskdf43fasdjl'))


def get_proxies():
    regex_ip = re.compile(r'<td data-title="IP">([.0-9]+?)</td>')
    regex_port = re.compile(r'<td data-title="PORT">(\d+)</td>')
    proxies_list = []
    try:
        #html_content = requests.get('https://www.kuaidaili.com/free/inha/' + str(random.randint(1, 12))).content.decode('utf-8')
        html_content = requests.get('https://www.kuaidaili.com/free/intr/' + str(random.randint(1, 12))).content.decode('utf-8')
        ip_list = regex_ip.findall(html_content)
        port_list = regex_port.findall(html_content)
        #print(ip_list, len(ip_list), port_list, len(port_list))
        for ip_port in zip(ip_list, port_list):
            proxies_list.append(ip_port[0] + ':' + ip_port[1])
        return proxies_list
    except:
        print("get proxy ip error!")
        proxies_list.append('125.126.203.37:9999');
        return

def get_proxies2():
    regex_ip = re.compile(b'<br>([.0-9:]+?)@HTTP')
    proxies_list = []
    # try:
    html_content = requests.get('http://ip.zdaye.com/dayProxy/ip/311886.html', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9",
            'Connection': 'keep-alive'}).content.decode('gb2312')
    print(html_content)
    ip_list = regex_ip.findall(html_content)

    return ip_list
    # except:
    #     print("get proxy ip error!")
    #     proxies_list.append('125.126.203.37:9999');
    #     return

def get_proxies3():
    return [
        '221.2.174.99:8060',
        '202.112.237.102:3128',
        '112.109.198.118:3128',
        '101.71.41.169:443',
        '121.8.98.196:80',
        '183.136.163.92:8080',
        '218.57.146.212:8888',
        '117.141.215.3:1080',
        '61.142.176.17:8082',
        '120.194.18.90:81',
        '221.4.172.162:3128',
        '120.234.63.196:3128',
        '116.114.19.204:443',
        '111.231.87.160:8088',
        '210.5.10.87:53281',
        '119.180.169.184:8060',
        '121.8.98.197:80',
        '123.207.68.166:1080',
        '221.2.175.238:8060',
        '27.129.50.242:3128',
        '58.240.53.194:8080',
        '14.21.22.250:3128',
        '47.98.168.204:8080',
        '119.57.108.53:53281',
        '27.208.184.126:8060',
        '120.79.99.27:80',
        '101.37.20.241:443',
        '221.210.120.153:54402',
        '58.240.53.197:80',
        '123.207.218.215:1080',
        '124.172.232.49:8010',
        '112.109.205.70:8118',
        '222.170.101.98:50204',
        '218.28.58.150:53281',
        '60.216.101.46:32868',
        '125.72.70.46:8060',
        '116.209.59.181:9999',
        '183.158.0.186:9999',
        '61.178.238.122:63000',
        '114.252.204.33:8060',
        '60.186.77.89:9999',
        '121.69.37.6:9797',
        '221.239.86.26:32228',
        '116.209.54.120:9999',
        '140.143.152.93:1080',
        '175.10.45.59:8060',
        '116.209.52.6:9999',
        '221.6.32.206:41816',
        '116.209.52.185:9999',
        '116.113.27.170:53889',
        '123.207.217.179:1080',
        '103.40.48.193:83',
        '116.209.54.170:9999',
        '203.110.164.139:52144',
        '183.63.101.62:55555',
        '116.209.61.224:9999',
        '116.209.56.56:9999',
        '116.209.56.73:9999',
        '110.102.37.169:8080',
        '121.69.46.178:9000',
        '115.28.179.51:80',
        '111.177.171.7:9999',
        '163.204.240.25:9999',
        '27.158.162.221:53281',
        '116.196.90.176:3128',
        '182.92.105.136:3128',
        '95.65.79.119:53281',
        '58.244.192.199:8080',
        '118.190.95.35:9001',
        '61.163.247.10:8118',
        '163.204.241.252:9999',
        '60.13.42.75:9999',
        '45.221.77.82:8080',
        '124.232.133.199:3128',
        '163.125.252.234:9797',
        '116.209.58.179:9999',
        '103.235.199.46:31611',
        '119.29.177.120:1080',
        '117.114.149.66:53281',
        '140.143.142.200:1080',
        '58.87.98.150:1080',
        '163.125.252.232:9797',
        '116.209.57.82:9999',
        '163.125.233.129:8088',
        '45.115.174.234:8080',
        '117.191.11.105:80',
        '47.95.201.41:3128',
        '58.52.83.65:9999',
        '182.150.35.173:80',
        '115.231.5.230:44524',
        '115.159.206.249:80',
        '61.183.176.122:57210',
        '39.137.168.230:80',
        '113.12.202.50:50327',
        '60.205.229.126:80',
        '116.209.55.144:9999',
        '175.23.72.67:8080',
        '218.77.183.125:8080',
        '116.204.155.16:8080',
        '221.1.200.242:61957',
    ]

if __name__ == '__main__':
    print(get_proxies())