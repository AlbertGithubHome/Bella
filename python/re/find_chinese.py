#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# find the line of containing chinese in files

__author__ = 'AlbertS'

import re

def start_find_chinese():
    find_count = 0;
    with open('strkey_ko_untranslate.txt', 'wb') as outfile:
        with open('strkey_ko.txt', 'rb') as infile:
            while True:
                content = infile.readline()
                if re.match(r'(.*[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+.*)', content.decode('utf-8')):
                    outfile.write(content)
                    find_count += 1;

                if not content:
                    return find_count

# start to crawler
if __name__ == '__main__':
    count = start_find_chinese()
    print("find complete! count =", count)
