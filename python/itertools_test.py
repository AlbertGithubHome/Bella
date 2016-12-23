#itertools test

#count
import itertools
naturals = itertools.count(2)

for n in naturals:
    print(n)
    if n > 10:
        break

#cycle
cs = itertools.cycle('ABC')
for c in cs:
    print(c)
    if c > 'B':
        break

print('abcdedfg' * 10)

#repeat
ns = itertools.repeat('ABC', 10)
for n in ns:
    print(n)

#takewhile
naturals = itertools.count(10)
ns = itertools.takewhile(lambda x : x <=20, naturals)
print(list(ns))