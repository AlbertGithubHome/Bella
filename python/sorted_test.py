#filter test

L = [36, 5, -12, 0, 34, 9, -21]
print('L =', L)


print('sorted(L) = ', sorted(L))


print('sorted(L, key = abs) = ', sorted(L, key = abs))


print('sorted(L, key = abs, reverse = True) = ', sorted(L, key = abs, reverse = True))

L = ['bob', 'about', 'Zoo', 'Credit']
print('sorted(L, key = str.lower, reverse = True) = ', sorted(L, key = str.lower, reverse = True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print('sorted(L, key = lambda x : x[1], reverse = True) = ', sorted(L, key = lambda x : x[1], reverse = True))