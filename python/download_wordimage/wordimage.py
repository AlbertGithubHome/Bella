# -*- coding: utf-8 -*-
# @Date     : 2018-08-20 10:31:45
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : crawl pictures with simple browser

import urllib.request, os

'''
http://www.171english.cn/renai/7a/ebook/images/136.jpg
http://www.171english.cn/renai/7a/ebook/images/130.jpg
129-137
125-134
130-137
130-137
127-135
'''

# save file path
target_path = "word_images/"
# target url that needs to crawler
target_url = "http://www.171english.cn/renai/{0}/ebook/images/{1}.jpg"

def get_file_local_path(catogery, page):
    return target_path + catogery + "_" + str(page) + ".jpg"

def start_crawler():
    #create dir if not exist
    if not os.path.isdir(target_path):
        os.mkdir(target_path)

    catogery_list = ['7a', '7b', '8a', '8b', '9a']
    for catogery in catogery_list:
        for page in range(125,138):
            try:
                full_file_name = get_file_local_path(catogery, page)
                urllib.request.urlretrieve(target_url.format(catogery, page), full_file_name)
                print("{0} download success!".format(full_file_name))
            except:
                passc

# start to crawler
if __name__ == '__main__':
    start_crawler()


# crawler result:
'''
word_images/7a_125.jpg download success!
word_images/7a_126.jpg download success!
word_images/7a_127.jpg download success!
word_images/7a_128.jpg download success!
word_images/7a_129.jpg download success!
word_images/7a_130.jpg download success!
word_images/7a_131.jpg download success!
word_images/7a_132.jpg download success!
word_images/7a_133.jpg download success!
word_images/7a_134.jpg download success!
word_images/7a_135.jpg download success!
word_images/7a_136.jpg download success!
word_images/7a_137.jpg download success!
word_images/7b_125.jpg download success!
word_images/7b_126.jpg download success!
word_images/7b_127.jpg download success!
word_images/7b_128.jpg download success!
word_images/7b_129.jpg download success!
word_images/7b_130.jpg download success!
word_images/7b_131.jpg download success!
word_images/7b_132.jpg download success!
word_images/7b_133.jpg download success!
word_images/7b_134.jpg download success!
word_images/7b_135.jpg download success!
word_images/7b_136.jpg download success!
word_images/7b_137.jpg download success!
word_images/8a_125.jpg download success!
word_images/8a_126.jpg download success!
word_images/8a_127.jpg download success!
word_images/8a_128.jpg download success!
word_images/8a_129.jpg download success!
word_images/8a_130.jpg download success!
word_images/8a_131.jpg download success!
word_images/8a_132.jpg download success!
word_images/8a_133.jpg download success!
word_images/8a_134.jpg download success!
word_images/8a_135.jpg download success!
word_images/8a_136.jpg download success!
word_images/8a_137.jpg download success!
word_images/8b_125.jpg download success!
word_images/8b_126.jpg download success!
word_images/8b_127.jpg download success!
word_images/8b_128.jpg download success!
word_images/8b_129.jpg download success!
word_images/8b_130.jpg download success!
word_images/8b_131.jpg download success!
word_images/8b_132.jpg download success!
word_images/8b_133.jpg download success!
word_images/8b_134.jpg download success!
word_images/8b_135.jpg download success!
word_images/8b_136.jpg download success!
word_images/8b_137.jpg download success!
word_images/9a_125.jpg download success!
word_images/9a_126.jpg download success!
word_images/9a_127.jpg download success!
word_images/9a_128.jpg download success!
word_images/9a_129.jpg download success!
word_images/9a_130.jpg download success!
word_images/9a_131.jpg download success!
word_images/9a_132.jpg download success!
word_images/9a_133.jpg download success!
word_images/9a_134.jpg download success!
word_images/9a_135.jpg download success!
word_images/9a_136.jpg download success!
word_images/9a_137.jpg download success!
[Finished in 4602.5s]

'''