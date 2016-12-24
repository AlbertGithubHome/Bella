# crawler re test
import re

source_str = '<img src="http://images.csdn.net/20161222/500004252-03-01.jpg">'
source_stt = '<img width="265" src="https://img5.doubanio.com/img/files/file-1431585796.jpg">'
source_stt = '<img src="https://img5.doubanio.com/file/view/ark_article_cover/28784360.jpg"'
source_stt = '<img src="https://img3.doubanio.com/view/ark_article_cover/large/public/28784360.jpg"'

all_ret = re.findall(r'(http:[\S]*?(jpg|png|gif))', source_str)

print(len(all_ret))

for n in all_ret:
    print(n[0])

import re

key = r"<html><body><h1>hello world<h1></body></html>"
p1 = r"(?<=<h1>).+?(?=<h1>)"
matcher = re.findall(p1, key)
print(matcher)



data = '<a href="/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143161198846783e33de56d4041058c3dfc7e44ee1203000">Python解释器</a>'
#url_set = set(re.findall(r'(?<=wiki).+(?=">))', data))
url_set = re.findall(r'((wiki/)[\S]*(?="))', data)
print(url_set)