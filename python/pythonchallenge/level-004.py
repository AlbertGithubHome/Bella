#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-04-17 19:33:41
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 4 of python challenge
# 
# 思路：这一关一开始想简单了，后来又想复杂了，前后用了大约30分钟，其中编码10分钟，调试出结果20分钟
#       首先打开这一关的源代码发现其中有一个链接<a href="linkedlist.php?nothing=12345">
#       访问这个链接发现一个新页面，其中只有几个文字and the next nothing is 44827
#       至此应该是循环查找答案，使用新得到的数字替换url中的数字，然后不断得到新的内容
#       第一个页面的源码中还有一句话<!-- urllib may help. DON'T TRY ALL NOTHINGS, 
#       since it will never end. 400 times is more than enough. -->
#       由此可知运行400次应该会有结果，于是我匹配页面中的数字，不断循环运行了400次
#       然后查看第398,399,400,401,402几个页面，发现一无所获
#       看来一开始还是想简单了，这个肯定有什么机密，于是我把循环所得的内容都打印了出来
#       这次发现了一下不一样的：
#       4 : <font color=red>Your hands are getting tired </font>and the next nothing is 94485 提醒手动会累死
#       87 : Yes. Divide by two and keep going. 居然还有一个没数字的
#       358 : peak.html 又发现一个没数字的，但这个就是答案，也就是说linkedlist.php?nothing=也可以正常访问页面
#       也就是这个链接导致了后面会无限循环，看来也没后来想的那么难
#       
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/def/linkedlist.php
#       3. next level url : http://www.pythonchallenge.com/pc/def/peak.html

import requests
import re

# entrance url
target_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

# get html page source code
def get_html_source_code(combine_url):
    html = requests.get(combine_url).content
    return html.decode('utf8');

def find_next_url(code_str):
    letter_list = re.findall(r'(\d*)', code_str)
    return ''.join(letter_list)

def main():
    try_count = 1
    nothing_value = '12345';
    html_content = ''
    while try_count < 403:
        print('%5d : nothing_value is %s, %s' % (try_count, nothing_value, html_content))
        html_content = get_html_source_code(target_url + nothing_value);
        nothing_value = find_next_url(html_content)
        try_count = try_count + 1;

if __name__ == '__main__':
    main()

# 运行结果
'''
    1 : nothing_value is 12345, 
    2 : nothing_value is 44827, and the next nothing is 44827
    3 : nothing_value is 45439, and the next nothing is 45439
    4 : nothing_value is 94485, <font color=red>Your hands are getting tired </font>and the next nothing is 94485
    5 : nothing_value is 72198, and the next nothing is 72198
    6 : nothing_value is 80992, and the next nothing is 80992
    7 : nothing_value is 8880, and the next nothing is 8880
    8 : nothing_value is 40961, and the next nothing is 40961
    9 : nothing_value is 58765, and the next nothing is 58765
   10 : nothing_value is 46561, and the next nothing is 46561
   11 : nothing_value is 13418, and the next nothing is 13418
   12 : nothing_value is 41954, and the next nothing is 41954
   13 : nothing_value is 46782, and the next nothing is 46782
   14 : nothing_value is 92730, and the next nothing is 92730
   15 : nothing_value is 89229, and the next nothing is 89229
   16 : nothing_value is 25646, and the next nothing is 25646
   17 : nothing_value is 74288, and the next nothing is 74288
   18 : nothing_value is 25945, and the next nothing is 25945
   19 : nothing_value is 39876, and the next nothing is 39876
   20 : nothing_value is 8498, and the next nothing is 8498
   21 : nothing_value is 34684, and the next nothing is 34684
   22 : nothing_value is 62316, and the next nothing is 62316
   23 : nothing_value is 71331, and the next nothing is 71331
   24 : nothing_value is 59717, and the next nothing is 59717
   25 : nothing_value is 76893, and the next nothing is 76893
   26 : nothing_value is 44091, and the next nothing is 44091
   27 : nothing_value is 73241, and the next nothing is 73241
   28 : nothing_value is 19242, and the next nothing is 19242
   29 : nothing_value is 17476, and the next nothing is 17476
   30 : nothing_value is 39566, and the next nothing is 39566
   31 : nothing_value is 81293, and the next nothing is 81293
   32 : nothing_value is 25857, and the next nothing is 25857
   33 : nothing_value is 74343, and the next nothing is 74343
   34 : nothing_value is 39410, and the next nothing is 39410
   35 : nothing_value is 5505, and the next nothing is 5505
   36 : nothing_value is 27104, and the next nothing is 27104
   37 : nothing_value is 54003, and the next nothing is 54003
   38 : nothing_value is 23501, and the next nothing is 23501
   39 : nothing_value is 21110, and the next nothing is 21110
   40 : nothing_value is 88399, and the next nothing is 88399
   41 : nothing_value is 49740, and the next nothing is 49740
   42 : nothing_value is 31552, and the next nothing is 31552
   43 : nothing_value is 39998, and the next nothing is 39998
   44 : nothing_value is 19755, and the next nothing is 19755
   45 : nothing_value is 64624, and the next nothing is 64624
   46 : nothing_value is 37817, and the next nothing is 37817
   47 : nothing_value is 43427, and the next nothing is 43427
   48 : nothing_value is 15115, and the next nothing is 15115
   49 : nothing_value is 44327, and the next nothing is 44327
   50 : nothing_value is 7715, and the next nothing is 7715
   51 : nothing_value is 15248, and the next nothing is 15248
   52 : nothing_value is 61895, and the next nothing is 61895
   53 : nothing_value is 54759, and the next nothing is 54759
   54 : nothing_value is 54270, and the next nothing is 54270
   55 : nothing_value is 51332, and the next nothing is 51332
   56 : nothing_value is 63481, and the next nothing is 63481
   57 : nothing_value is 12362, and the next nothing is 12362
   58 : nothing_value is 94476, and the next nothing is 94476
   59 : nothing_value is 87810, and the next nothing is 87810
   60 : nothing_value is 6027, and the next nothing is 6027
   61 : nothing_value is 47551, and the next nothing is 47551
   62 : nothing_value is 79498, and the next nothing is 79498
   63 : nothing_value is 81226, and the next nothing is 81226
   64 : nothing_value is 4256, and the next nothing is 4256
   65 : nothing_value is 62734, and the next nothing is 62734
   66 : nothing_value is 25666, and the next nothing is 25666
   67 : nothing_value is 14781, and the next nothing is 14781
   68 : nothing_value is 21412, and the next nothing is 21412
   69 : nothing_value is 55205, and the next nothing is 55205
   70 : nothing_value is 65516, and the next nothing is 65516
   71 : nothing_value is 53535, and the next nothing is 53535
   72 : nothing_value is 4437, and the next nothing is 4437
   73 : nothing_value is 43442, and the next nothing is 43442
   74 : nothing_value is 91308, and the next nothing is 91308
   75 : nothing_value is 1312, and the next nothing is 1312
   76 : nothing_value is 36268, and the next nothing is 36268
   77 : nothing_value is 34289, and the next nothing is 34289
   78 : nothing_value is 46384, and the next nothing is 46384
   79 : nothing_value is 18097, and the next nothing is 18097
   80 : nothing_value is 9401, and the next nothing is 9401
   81 : nothing_value is 54249, and the next nothing is 54249
   82 : nothing_value is 29247, and the next nothing is 29247
   83 : nothing_value is 13115, and the next nothing is 13115
   84 : nothing_value is 23053, and the next nothing is 23053
   85 : nothing_value is 3875, and the next nothing is 3875
   86 : nothing_value is 16044, and the next nothing is 16044
   87 : nothing_value is , Yes. Divide by two and keep going.
   88 : nothing_value is 72758, and the next nothing is 72758
   89 : nothing_value is 71301, and the next nothing is 71301
   90 : nothing_value is 55577, and the next nothing is 55577
   91 : nothing_value is 88786, and the next nothing is 88786
   92 : nothing_value is 32293, and the next nothing is 32293
   93 : nothing_value is 87798, and the next nothing is 87798
   94 : nothing_value is 24838, and the next nothing is 24838
   95 : nothing_value is 66137, and the next nothing is 66137
   96 : nothing_value is 88016, and the next nothing is 88016
   97 : nothing_value is 36876, and the next nothing is 36876
   98 : nothing_value is 33179, and the next nothing is 33179
   99 : nothing_value is 90231, and the next nothing is 90231
  100 : nothing_value is 17825, and the next nothing is 17825
  101 : nothing_value is 84361, and the next nothing is 84361
  102 : nothing_value is 99222, and the next nothing is 99222
  103 : nothing_value is 87348, and the next nothing is 87348
  104 : nothing_value is 47100, and the next nothing is 47100
  105 : nothing_value is 90650, and the next nothing is 90650
  106 : nothing_value is 84369, and the next nothing is 84369
  107 : nothing_value is 36116, and the next nothing is 36116
  108 : nothing_value is 96544, and the next nothing is 96544
  109 : nothing_value is 62892, and the next nothing is 62892
  110 : nothing_value is 43790, and the next nothing is 43790
  111 : nothing_value is 67652, and the next nothing is 67652
  112 : nothing_value is 32839, and the next nothing is 32839
  113 : nothing_value is 5353, and the next nothing is 5353
  114 : nothing_value is 63153, and the next nothing is 63153
  115 : nothing_value is 48029, and the next nothing is 48029
  116 : nothing_value is 84141, and the next nothing is 84141
  117 : nothing_value is 14662, and the next nothing is 14662
  118 : nothing_value is 78566, and the next nothing is 78566
  119 : nothing_value is 18131, and the next nothing is 18131
  120 : nothing_value is 710, and the next nothing is 710
  121 : nothing_value is 67500, and the next nothing is 67500
  122 : nothing_value is 34992, and the next nothing is 34992
  123 : nothing_value is 64568, and the next nothing is 64568
  124 : nothing_value is 8155, and the next nothing is 8155
  125 : nothing_value is 30579, and the next nothing is 30579
  126 : nothing_value is 11629, and the next nothing is 11629
  127 : nothing_value is 32490, and the next nothing is 32490
  128 : nothing_value is 47936, and the next nothing is 47936
  129 : nothing_value is 51350, and the next nothing is 51350
  130 : nothing_value is 51877, and the next nothing is 51877
  131 : nothing_value is 38270, and the next nothing is 38270
  132 : nothing_value is 41643, and the next nothing is 41643
  133 : nothing_value is 23416, and the next nothing is 23416
  134 : nothing_value is 54432, and the next nothing is 54432
  135 : nothing_value is 4448, and the next nothing is 4448
  136 : nothing_value is 30086, and the next nothing is 30086
  137 : nothing_value is 93346, and the next nothing is 93346
  138 : nothing_value is 53491, and the next nothing is 53491
  139 : nothing_value is 31248, and the next nothing is 31248
  140 : nothing_value is 37446, and the next nothing is 37446
  141 : nothing_value is 11309, and the next nothing is 11309
  142 : nothing_value is 13878, and the next nothing is 13878
  143 : nothing_value is 31404, and the next nothing is 31404
  144 : nothing_value is 27786, and the next nothing is 27786
  145 : nothing_value is 16030, and the next nothing is 16030
  146 : nothing_value is 4689, and the next nothing is 4689
  147 : nothing_value is 16553, and the next nothing is 16553
  148 : nothing_value is 98150, and the next nothing is 98150
  149 : nothing_value is 19224, and the next nothing is 19224
  150 : nothing_value is 71919, and the next nothing is 71919
  151 : nothing_value is 53068, and the next nothing is 53068
  152 : nothing_value is 71407, and the next nothing is 71407
  153 : nothing_value is 54264, and the next nothing is 54264
  154 : nothing_value is 33407, and the next nothing is 33407
  155 : nothing_value is 11086, and the next nothing is 11086
  156 : nothing_value is 72527, and the next nothing is 72527
  157 : nothing_value is 92923, and the next nothing is 92923
  158 : nothing_value is 93389, and the next nothing is 93389
  159 : nothing_value is 94438, and the next nothing is 94438
  160 : nothing_value is 88796, and the next nothing is 88796
  161 : nothing_value is 90785, and the next nothing is 90785
  162 : nothing_value is 73079, and the next nothing is 73079
  163 : nothing_value is 75559, and the next nothing is 75559
  164 : nothing_value is 53223, and the next nothing is 53223
  165 : nothing_value is 75979, and the next nothing is 75979
  166 : nothing_value is 55749, and the next nothing is 55749
  167 : nothing_value is 52948, and the next nothing is 52948
  168 : nothing_value is 71569, and the next nothing is 71569
  169 : nothing_value is 10240, and the next nothing is 10240
  170 : nothing_value is 3064, and the next nothing is 3064
  171 : nothing_value is 29818, and the next nothing is 29818
  172 : nothing_value is 88835, and the next nothing is 88835
  173 : nothing_value is 38200, and the next nothing is 38200
  174 : nothing_value is 32515, and the next nothing is 32515
  175 : nothing_value is 43551, and the next nothing is 43551
  176 : nothing_value is 1398, and the next nothing is 1398
  177 : nothing_value is 23580, and the next nothing is 23580
  178 : nothing_value is 31619, and the next nothing is 31619
  179 : nothing_value is 83052, and the next nothing is 83052
  180 : nothing_value is 37409, and the next nothing is 37409
  181 : nothing_value is 85052, and the next nothing is 85052
  182 : nothing_value is 13510, and the next nothing is 13510
  183 : nothing_value is 43240, and the next nothing is 43240
  184 : nothing_value is 5868, and the next nothing is 5868
  185 : nothing_value is 19337, and the next nothing is 19337
  186 : nothing_value is 21122, and the next nothing is 21122
  187 : nothing_value is 92118, and the next nothing is 92118
  188 : nothing_value is 44659, and the next nothing is 44659
  189 : nothing_value is 60291, and the next nothing is 60291
  190 : nothing_value is 29895, and the next nothing is 29895
  191 : nothing_value is 98452, and the next nothing is 98452
  192 : nothing_value is 42243, and the next nothing is 42243
  193 : nothing_value is 25755, and the next nothing is 25755
  194 : nothing_value is 28879, and the next nothing is 28879
  195 : nothing_value is 37149, and the next nothing is 37149
  196 : nothing_value is 17033, and the next nothing is 17033
  197 : nothing_value is 543, and the next nothing is 543
  198 : nothing_value is 82304, and the next nothing is 82304
  199 : nothing_value is 80616, and the next nothing is 80616
  200 : nothing_value is 36217, and the next nothing is 36217
  201 : nothing_value is 16201, and the next nothing is 16201
  202 : nothing_value is 33304, and the next nothing is 33304
  203 : nothing_value is 20091, and the next nothing is 20091
  204 : nothing_value is 93295, and the next nothing is 93295
  205 : nothing_value is 75485, and the next nothing is 75485
  206 : nothing_value is 1765, and the next nothing is 1765
  207 : nothing_value is 76626, and the next nothing is 76626
  208 : nothing_value is 92820, and the next nothing is 92820
  209 : nothing_value is 52222, and the next nothing is 52222
  210 : nothing_value is 2892, and the next nothing is 2892
  211 : nothing_value is 65776, and the next nothing is 65776
  212 : nothing_value is 817, and the next nothing is 817
  213 : nothing_value is 2025, and the next nothing is 2025
  214 : nothing_value is 94455, and the next nothing is 94455
  215 : nothing_value is 47579, and the next nothing is 47579
  216 : nothing_value is 56908, and the next nothing is 56908
  217 : nothing_value is 39768, and the next nothing is 39768
  218 : nothing_value is 76810, and the next nothing is 76810
  219 : nothing_value is 36875, and the next nothing is 36875
  220 : nothing_value is 97644, and the next nothing is 97644
  221 : nothing_value is 84602, and the next nothing is 84602
  222 : nothing_value is 86446, and the next nothing is 86446
  223 : nothing_value is 71359, and the next nothing is 71359
  224 : nothing_value is 33883, and the next nothing is 33883
  225 : nothing_value is 70553, and the next nothing is 70553
  226 : nothing_value is 98832, and the next nothing is 98832
  227 : nothing_value is 60599, and the next nothing is 60599
  228 : nothing_value is 17342, and the next nothing is 17342
  229 : nothing_value is 74423, and the next nothing is 74423
  230 : nothing_value is 41609, and the next nothing is 41609
  231 : nothing_value is 54377, and the next nothing is 54377
  232 : nothing_value is 33490, and the next nothing is 33490
  233 : nothing_value is 35815, and the next nothing is 35815
  234 : nothing_value is 59166, and the next nothing is 59166
  235 : nothing_value is 11441, and the next nothing is 11441
  236 : nothing_value is 94796, and the next nothing is 94796
  237 : nothing_value is 68509, and the next nothing is 68509
  238 : nothing_value is 45872, and the next nothing is 45872
  239 : nothing_value is 81664, and the next nothing is 81664
  240 : nothing_value is 94537, and the next nothing is 94537
  241 : nothing_value is 36571, and the next nothing is 36571
  242 : nothing_value is 52815, and the next nothing is 52815
  243 : nothing_value is 54533, and the next nothing is 54533
  244 : nothing_value is 74595, and the next nothing is 74595
  245 : nothing_value is 55654, and the next nothing is 55654
  246 : nothing_value is 48550, and the next nothing is 48550
  247 : nothing_value is 56044, and the next nothing is 56044
  248 : nothing_value is 25536, and the next nothing is 25536
  249 : nothing_value is 30479, and the next nothing is 30479
  250 : nothing_value is 77512, and the next nothing is 77512
  251 : nothing_value is 94866, and the next nothing is 94866
  252 : nothing_value is 26746, and the next nothing is 26746
  253 : nothing_value is 44833, and the next nothing is 44833
  254 : nothing_value is 96169, and the next nothing is 96169
  255 : nothing_value is 73807, and the next nothing is 73807
  256 : nothing_value is 65481, and the next nothing is 65481
  257 : nothing_value is 28520, and the next nothing is 28520
  258 : nothing_value is 71069, and the next nothing is 71069
  259 : nothing_value is 40951, and the next nothing is 40951
  260 : nothing_value is 72828, and the next nothing is 72828
  261 : nothing_value is 80158, and the next nothing is 80158
  262 : nothing_value is 22504, and the next nothing is 22504
  263 : nothing_value is 69881, and the next nothing is 69881
  264 : nothing_value is 15695, and the next nothing is 15695
  265 : nothing_value is 49718, and the next nothing is 49718
  266 : nothing_value is 64436, and the next nothing is 64436
  267 : nothing_value is 27671, and the next nothing is 27671
  268 : nothing_value is 44306, and the next nothing is 44306
  269 : nothing_value is 59668, and the next nothing is 59668
  270 : nothing_value is 52257, and the next nothing is 52257
  271 : nothing_value is 7219, and the next nothing is 7219
  272 : nothing_value is 36882, and the next nothing is 36882
  273 : nothing_value is 48246, and the next nothing is 48246
  274 : nothing_value is 10907, and the next nothing is 10907
  275 : nothing_value is 57291, and the next nothing is 57291
  276 : nothing_value is 15565, and the next nothing is 15565
  277 : nothing_value is 40253, and the next nothing is 40253
  278 : nothing_value is 57887, and the next nothing is 57887
  279 : nothing_value is 75107, and the next nothing is 75107
  280 : nothing_value is 4757, and the next nothing is 4757
  281 : nothing_value is 3219, and the next nothing is 3219
  282 : nothing_value is 84631, and the next nothing is 84631
  283 : nothing_value is 75550, and the next nothing is 75550
  284 : nothing_value is 30793, and the next nothing is 30793
  285 : nothing_value is 30982, and the next nothing is 30982
  286 : nothing_value is 4391, and the next nothing is 4391
  287 : nothing_value is 86607, and the next nothing is 86607
  288 : nothing_value is 41433, and the next nothing is 41433
  289 : nothing_value is 97107, and the next nothing is 97107
  290 : nothing_value is 89858, and the next nothing is 89858
  291 : nothing_value is 186, and the next nothing is 186
  292 : nothing_value is 37842, and the next nothing is 37842
  293 : nothing_value is 2777, and the next nothing is 2777
  294 : nothing_value is 44508, and the next nothing is 44508
  295 : nothing_value is 48314, and the next nothing is 48314
  296 : nothing_value is 48355, and the next nothing is 48355
  297 : nothing_value is 67280, and the next nothing is 67280
  298 : nothing_value is 852, and the next nothing is 852
  299 : nothing_value is 6756, and the next nothing is 6756
  300 : nothing_value is 93964, and the next nothing is 93964
  301 : nothing_value is 51422, and the next nothing is 51422
  302 : nothing_value is 82972, and the next nothing is 82972
  303 : nothing_value is 20192, and the next nothing is 20192
  304 : nothing_value is 12568, and the next nothing is 12568
  305 : nothing_value is 33780, and the next nothing is 33780
  306 : nothing_value is 28995, and the next nothing is 28995
  307 : nothing_value is 94122, and the next nothing is 94122
  308 : nothing_value is 13677, and the next nothing is 13677
  309 : nothing_value is 78020, and the next nothing is 78020
  310 : nothing_value is 50718, and the next nothing is 50718
  311 : nothing_value is 3014, and the next nothing is 3014
  312 : nothing_value is 87513, and the next nothing is 87513
  313 : nothing_value is 60592, and the next nothing is 60592
  314 : nothing_value is 16613, and the next nothing is 16613
  315 : nothing_value is 48784, and the next nothing is 48784
  316 : nothing_value is 91727, and the next nothing is 91727
  317 : nothing_value is 81823, and the next nothing is 81823
  318 : nothing_value is 92306, and the next nothing is 92306
  319 : nothing_value is 82052, and the next nothing is 82052
  320 : nothing_value is 99401, and the next nothing is 99401
  321 : nothing_value is 2228, and the next nothing is 2228
  322 : nothing_value is 69304, and the next nothing is 69304
  323 : nothing_value is 36845, and the next nothing is 36845
  324 : nothing_value is 72224, and the next nothing is 72224
  325 : nothing_value is 84132, and the next nothing is 84132
  326 : nothing_value is 92376, and the next nothing is 92376
  327 : nothing_value is 40503, and the next nothing is 40503
  328 : nothing_value is 67329, and the next nothing is 67329
  329 : nothing_value is 56881, and the next nothing is 56881
  330 : nothing_value is 72156, and the next nothing is 72156
  331 : nothing_value is 46463, and the next nothing is 46463
  332 : nothing_value is 62058, and the next nothing is 62058
  333 : nothing_value is 54696, and the next nothing is 54696
  334 : nothing_value is 65731, and the next nothing is 65731
  335 : nothing_value is 38290, and the next nothing is 38290
  336 : nothing_value is 57913, and the next nothing is 57913
  337 : nothing_value is 6309, and the next nothing is 6309
  338 : nothing_value is 73902, and the next nothing is 73902
  339 : nothing_value is 19934, and the next nothing is 19934
  340 : nothing_value is 16055, and the next nothing is 16055
  341 : nothing_value is 50563, and the next nothing is 50563
  342 : nothing_value is 47825, and the next nothing is 47825
  343 : nothing_value is 73265, and the next nothing is 73265
  344 : nothing_value is 90961, and the next nothing is 90961
  345 : nothing_value is 29740, and the next nothing is 29740
  346 : nothing_value is 43628, and the next nothing is 43628
  347 : nothing_value is 11088, and the next nothing is 11088
  348 : nothing_value is 93781, and the next nothing is 93781
  349 : nothing_value is 55840, and the next nothing is 55840
  350 : nothing_value is 80842, and the next nothing is 80842
  351 : nothing_value is 59022, and the next nothing is 59022
  352 : nothing_value is 23298, and the next nothing is 23298
  353 : nothing_value is 27709, and the next nothing is 27709
  354 : nothing_value is 96791, and the next nothing is 96791
  355 : nothing_value is 75635, and the next nothing is 75635
  356 : nothing_value is 52899, and the next nothing is 52899
  357 : nothing_value is 66831, and the next nothing is 66831
  358 : nothing_value is , peak.html
  359 : nothing_value is 72758, and the next nothing is 72758
  360 : nothing_value is 71301, and the next nothing is 71301
  361 : nothing_value is 55577, and the next nothing is 55577
  362 : nothing_value is 88786, and the next nothing is 88786
  363 : nothing_value is 32293, and the next nothing is 32293
  364 : nothing_value is 87798, and the next nothing is 87798
  365 : nothing_value is 24838, and the next nothing is 24838
  366 : nothing_value is 66137, and the next nothing is 66137
  367 : nothing_value is 88016, and the next nothing is 88016
  368 : nothing_value is 36876, and the next nothing is 36876
  369 : nothing_value is 33179, and the next nothing is 33179
  370 : nothing_value is 90231, and the next nothing is 90231
  371 : nothing_value is 17825, and the next nothing is 17825
  372 : nothing_value is 84361, and the next nothing is 84361
  373 : nothing_value is 99222, and the next nothing is 99222
  374 : nothing_value is 87348, and the next nothing is 87348
  375 : nothing_value is 47100, and the next nothing is 47100
  376 : nothing_value is 90650, and the next nothing is 90650
  377 : nothing_value is 84369, and the next nothing is 84369
  378 : nothing_value is 36116, and the next nothing is 36116
  379 : nothing_value is 96544, and the next nothing is 96544
  380 : nothing_value is 62892, and the next nothing is 62892
  381 : nothing_value is 43790, and the next nothing is 43790
  382 : nothing_value is 67652, and the next nothing is 67652
  383 : nothing_value is 32839, and the next nothing is 32839
  384 : nothing_value is 5353, and the next nothing is 5353
  385 : nothing_value is 63153, and the next nothing is 63153
  386 : nothing_value is 48029, and the next nothing is 48029
  387 : nothing_value is 84141, and the next nothing is 84141
  388 : nothing_value is 14662, and the next nothing is 14662
  389 : nothing_value is 78566, and the next nothing is 78566
  390 : nothing_value is 18131, and the next nothing is 18131
  391 : nothing_value is 710, and the next nothing is 710
  392 : nothing_value is 67500, and the next nothing is 67500
  393 : nothing_value is 34992, and the next nothing is 34992
  394 : nothing_value is 64568, and the next nothing is 64568
  395 : nothing_value is 8155, and the next nothing is 8155
  396 : nothing_value is 30579, and the next nothing is 30579
  397 : nothing_value is 11629, and the next nothing is 11629
  398 : nothing_value is 32490, and the next nothing is 32490
  399 : nothing_value is 47936, and the next nothing is 47936
  400 : nothing_value is 51350, and the next nothing is 51350
  401 : nothing_value is 51877, and the next nothing is 51877
  402 : nothing_value is 38270, and the next nothing is 38270
[Finished in 166.4s]
'''