#decorator test
p = lambda x: x * x
print('p(10) =', p(10))
print('p =', p)

print('p.__name__ =', p.__name__)

def myadd(x, y):
    return x + y

f = myadd

print('f.__name__ =', f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print()
        print('decorator --> call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#now = log(now)
@log
def now():
    print('2016-12-09')

now()

@log
def I():
    print('I am ...')

I()

import functools

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print()
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#now2 = log2('test')(now2)
@log2('test')
def now2():
    print('This is a now2')

now2()
print('\n', now2.__name__)









