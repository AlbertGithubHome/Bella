# -*- coding: utf-8 -*-

word = '好好'
print(type(word), word)

result = word.encode('utf-8')
print(type(result), result)

new_word = result.decode('gbk')
print(type(new_word), new_word)

data = b'\xe5\xa5\xbd\xe5\xa5\xbd'
print(type(data), data)

result = data.decode('utf-8')
print(type(result), result)

