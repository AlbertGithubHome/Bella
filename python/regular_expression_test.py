# regular expression test

import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

s = 'a b c  d e'
print(s.split(' '))
print(re.split(r'\s+', s))

print()
s = 'a b.c,  d; e'
print(s.split(' '))
print(re.split(r'[\s\;\,\.]+', s))


print()
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.groups())

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

#greed test
print()
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

#compile test
print()
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('123-5463453').groups())