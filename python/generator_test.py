#generator test

L = [x * x for x in range(1, 20 , 2)]
print('L = [x * x  for x in range(1, 20 , 2)] =', L)

g = (x * x for x in range(1, 20 , 2))
print('g = [x * x  for x in range(1, 20 , 2)] =', g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(32 * '-')
g = (x * 2 + 1 for x in range(1, 20 , 2))
for n in g:
    print(n)

a = 1
b = 2

a, b = b, a
print('a, b =', a, b)

#normal function vs generator
#normal function
def fib1(layer):
    x, y = 0, 1
    while layer > 0:
        print(y)
        x, y = y , x + y
        layer = layer - 1
    return 'done it'

print(32 * '-')
fib1(8)

#generator
def fib2(layer):
    x, y = 0, 1
    while layer > 0:
        yield(y)
        x, y = y , x + y
        layer = layer - 1
    return 'done it'

print(32 * '-')
ret = fib2(8)
next(ret)
next(ret)

print(32 * '-')
ret = fib2(4)
for b in ret:
    print(b)

print(32 * '-')
ret = fib2(10)

while True:
    try:
        x = next(ret)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
