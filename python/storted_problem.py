

#我是一个新手，第一次看这么复杂的代码，不过仔细分析一下可以理解
#源代码

s = input('please input string:')
freq = {}
for c in s:
    freq[c] = freq.setdefault(c, 0) + 1
print(','.join(sorted(freq, key=lambda x: (-freq[x], x))))


#等价于
'''
s = input('please input string:')           #提示输入一个字符串
freq = {}                                   #定义一个字典结构
for c in s:                                 #遍历输入的字符串
    freq[c] = freq.setdefault(c, 0) + 1     #在字典结构中查找，若之前没有设置为0 + 1，若已经存在则直接加1

sorted(freq, key=lambda x: (-freq[x], x))   #这里是排序，key的值是排序规则，
#如果是`freq[x]`默认是按照频度升序，所以使用`-freq[x]`表示使用频度负数排序，即变成了降序，后边还有一个x表示频度相同按字典排序
print(','.join(freq)#便是把排好的序列使用盗号分隔输出
'''