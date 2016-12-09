#lambda test

p = lambda x: x * x
print('p(10) =', p(10))
print('p =', p)

def func():
    return lambda x, y: x + y

myfunc = func()

print('myfunc =', myfunc)
print('myfunc() =', myfunc(4, 5))

