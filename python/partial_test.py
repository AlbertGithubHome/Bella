#partial test

s = '11'
print('s =', s)

print('int(s) =', int(s))
print('int(s, 10) =', int(s, 10))
print('int(s, 16) =', int(s, 16))
print('int(s, 8) =', int(s, 8))
print('int(s, 2) =', int(s, 2))

def int2(x, base = 2):
    return int(x, base)

ss = '111'
print()
print('int(ss) =', int(ss))
print('int2(ss) =', int2(ss))

import functools
int3 =functools.partial(int, base=2)

print()
print('int3(ss) =', int3(ss))