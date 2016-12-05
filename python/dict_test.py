# dict test

# like hash map
dic = {'XiaoMing' : 99, 'ZhangFei' : 80, 1 : 40, '1' : 50}
print('dic =', dic)

print(dic[1])

print(dic['XiaoMing'])

# Error! index error
# print(dic['XiaoHong'])
'''
Traceback (most recent call last):
  File "dict_test.py", line 12, in <module>
    print(dic['XiaoHong'])
KeyError: 'XiaoHong'
'''

dic['XiaoHei'] = 67
print('dic =', dic)

print(dic.get('XiaoHong'))

print(dic.get('XiaoHong'), ', Not Find XiaoHong')

# do pop
dic.pop('1')
print('dic =', dic)

# Error
#key = [1, 2, 3]
#dic[key] = 'a list' 
'''
Traceback (most recent call last):
  File "dict_test.py", line 33, in <module>
    dic[key] = 'a list'
TypeError: unhashable type: 'list'
'''