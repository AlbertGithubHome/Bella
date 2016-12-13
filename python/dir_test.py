#dir test

S = 'ABC'
print('S =', S)
print('dir(S) =', dir(S))

print('ABC'.__len__())
print(len('ABC'))


class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print('len(dog) =', len(dog))

print(hasattr(dog, 'x'))

setattr(dog, 'x', 10)
print(hasattr(dog, 'x'))
print(getattr(dog, 'x'))

# the attr is not exist
print(getattr(dog, 'y', 404))