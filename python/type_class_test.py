#use type() to create class
class Hello(object):
    def hello(self, name = 'world'):
        print('Hello %s' % name)


print('Hello =', Hello)

s = Hello()
print('s =', s)

print('type(Hello) =', type(Hello))
print('type(s) =', type(s))

#define class not use class descriptor
def func(self, name = 'world'):
    print('Hello %s' % name)

Hello2 = type('Hello2', (object, ), dict(hello=func))
print('type(Hello2) =', type(Hello2))
s2 = Hello2()
print('type(s2) =', type(s2))