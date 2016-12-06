#slice test

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('L =', L)


#list traverse
for i in L:
    print(i)

#dict itorater
print(32 * '-')
D = {'XiaoMing' : 90, 'XiaoWang' : 67}
print('D =', D)

for k in D:
    print('k =', k)

for v in D.values():
    print('v =', v)

for k, v in D.items():
    print('k, v =', k, v)

#string itorater
print(32 * '-')
Name = 'XiaoMing'
print('Name =', Name)

for s in Name:
    print(s)

# enumerate generate index
print(32 * '-')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

print(32 * '-')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

#check iterable
print(32 * '-')
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3,4], Iterable))
print(isinstance((1,2,3,4), Iterable))
print(isinstance(12324, Iterable))