#functon test

print('abs(-45) =', abs(-45))


print('max(-45, 1, 2, 89.9, 45) =', max(-45, 1, 2, 89.9, 45))

my_abs = abs
print('my_abs(-45) =', my_abs(-45))


print('bool(1>0) =', bool(1>0))

print('float(10) =', float(10))

print('hex(254) =', hex(254))

def myabs(x):
    if x >= 0:
        return x;
    else:
        return -x;

print('myabs(-45) =', myabs(-45))

def myfunc():
    pass
    print("pass")

myfunc()

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# return tuple
# (160.0,100.0)
x, y = move(100, 100, 60, 0)
print(x, y)

def calcpowsum(*numbers):
    sum = 0;
    for n in numbers:
        sum = sum + n * n
    return sum

print('calcpowsum(1, 2, 3) =', calcpowsum(1, 2, 3))

t =(1, 2, 3, 4)
print('calcpowsum(*t) =', calcpowsum(*t))

# dict argument
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# certain argument name, have two positional arguments
def newperson(name, age, *, city, job):
    print(name, age, city, job)
newperson('Jack', 24, city='Beijing', job='Engineer')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

#f1(1, 2, d=99, 23, c = 12, ext=None)
'''
E:\GitProject\Bella\python>H:\Python34\python function_test.py
  File "function_test.py", line 70
    f1(1, 2, d=99, 23, c = 12, ext=None)
                  ^
SyntaxError: non-keyword arg after keyword arg
'''
#order : 必选参数、默认参数、可变参数、命名关键字参数和关键字参
#order : required positional arg, default arg, variable arg, required keyword-only arg, keyword arg 

f1(1, 2, 99, 23, d = 12, ext=None)

def f2(a, b, c=0, *args, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f2(1, 2, 23, 34, d =99, e = 12, ext=None)

args = (1,2)
kw = {'d': 99, 'x': '#'}
f2(*args, **kw)
