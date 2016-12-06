#List Comprehensions test

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('L =', L)

L = list(range(1, 11))
print('L =', L)

L = [x * x for x in range(1, 20 , 2)]
print('L = [x * x  for x in range(1, 20 , 2)] =', L)

L = [x * x for x in range(1, 20 , 2) if x != 11]
print('L = [x * x  for x in range(1, 20 , 2) if x != 11] =', L)

L = [m + n for m in 'ABCD' for n in 'XYZ']
print('L = [m + n for m in \'ABCD\' for n in \'XYZ\'] =', L)


import os
L = [s for s in os.listdir('.')]
print('L = [s for s in os.listdir(".")] =', L)


L = ['Hello', 'World', 'IBM', 'Apple']
print('L =', L)
print('[s.lower() for s in L] =', [s.lower() for s in L])


L = ['Hello', 'World', 'IBM', 'Apple', 12, 'LOHds', None, 'As']
print('L =', L)
print('[s.lower() for s in L if isinstance(s, str)] =', [s.lower() for s in L if isinstance(s, str)])