#map test

L = [x for x in range(1, 20 , 1)]
print('L = [x * x  for x in range(1, 20 , 1)] =', L)

def power(x):
    return x * x

Ret = map(power, L)
print('Ret = ', Ret)
print('next(Ret) =', next(Ret))

print('list(Ret) =', list(Ret));