#slice test

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('L =', L)


#positive number
print(32 * '-')
print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])

print('L[1:3] =', L[1:3])

print('L[:] =', L[:])


#negative number
print(32 * '-')
print('L[-4:] =', L[-4:])

print('L[-4:4] =', L[-4:4])

print('L[-4:1] =', L[-4:1])
print('L[-2:] =', L[-2:])

#nterval index
print(32 * '-')
print('L[-4::2] =', L[-4::2])
print('L[::2] =', L[::2])


#string slice
print(32 * '-')
print('\'ABCDJSFL\'[:3]', 'ABCDJSFL'[:3])
print('\'ABCDJSFL\'[1:3]', 'ABCDJSFL'[1:3])
print('\'ABCDJSSSFL\'[::3]', 'ABCDJSSSFL'[::3])

#tuple slice
print(32 * '-')
t = (1, 2, 43, 6, 12, 7, 89)
print('t =', t)
print('t[:4:2] =', t[:4:2])