#feature test

# 1, 3, 5, 7,...,21
L = []
n = 1
while n <= 21:
    L.append(n)
    n = n + 2
print(L)


L2 = list(range(1, 22, 2))
print('L2 =', L2)


L3 = list(range(22))[1::2]
print('L3 =', L3)