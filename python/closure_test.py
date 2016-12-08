#closure test

def clac_sum(*args):
    ax = 0
    for n in argx:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


mysum = lazy_sum(1, 2, 3, 4)
print('mysum() =', mysum())
print('mysum =', mysum)

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print('f1() =', f1())
print('f2() =', f2())
print('f3() =', f3())

def count2():
    fs = []
    for i in range(1, 4):
        def xx(n):
            def f():
                return n * n
            return f
        fs.append(xx(i))
    return fs

f1, f2, f3 = count2()
print('f1() =', f1())
print('f2() =', f2())
print('f3() =', f3())
