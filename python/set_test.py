# dict test
# like hashtable but have not value

# not order
s = set([1,2,8,6,100])
print('s =', s)

# not duplicate

s2 = set([1,2,8,6, 2, 3, 6])
print('s2 =', s2)

s2.add(8)
s2.add('XiaoMing')
s2.add('Bella')
s2.add('Bella')
print('s2 =', s2)

s2.remove(8)
print('after remove 8 -- s2 =', s2)

#intersection
s3 = s & s2;
print('s3 = s & s2 -- s3 =', s3)

#union
s4 = s | s2;
print('s4 = s | s2 -- s4 =', s4)

s5 = set((1, 5, 9))
print('s5 =', s5)

s5.add((1, 2, 3))
print('s5 =', s5)

#s5.add((1, 5, [1, 2]))
#print('s6 =', s6)
'''
Traceback (most recent call last):
  File "set_test.py", line 36, in <module>
    s5.add((1, 5, [1, 2]))
TypeError: unhashable type: 'list'
'''