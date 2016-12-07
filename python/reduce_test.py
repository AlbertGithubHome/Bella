#reduce test

L = [x for x in range(1, 20 , 1)]
print('L = [x * x  for x in range(1, 20 , 1)] =', L)

def add(x, y):
    return x + y

from functools import reduce

Ret = reduce(add, L)
print('Ret = ', Ret)

# ERROR : TypeError: 'int' object is not iterable
# print('list(Ret) =', list(Ret));


def fn(x, y):
    return x * 10 + y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

listRet = map(char2num, '123435')
print('Ret =', reduce(fn, listRet))

# lambda expression
print('Lambda =', reduce(lambda x, y: 10 * x + y, map(char2num, '41324')))
