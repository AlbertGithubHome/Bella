#reduce test

L = [x for x in range(1, 20 , 1)]
print('L = [x * x  for x in range(1, 20 , 1)] =', L)

def my_remove(x):
    return x % 2 == 0

RET = filter(my_remove, L)
print('list(RET) =', list(RET))


# find primes
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

g_prime = primes()
print('next(g_prime) =', next(g_prime))
#print(list(g_prime))
#
for n in g_prime:
    if n < 10:
        print(n)
    else:
        break


def is_palindrome(n):
    target = str(n)
    tlen = len(target) // 2
    n = 0
    while n < tlen:
        if target[n] != target[-n - 1]:
            return False
        n = n + 1
    return True


output = filter(is_palindrome, range(1, 1000))
print(list(output))
#is_palindrome(123)