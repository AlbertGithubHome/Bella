#list test
print()
print('list test...')
classmates = ['Michael','Bob', 'Tracy']

print('classmates =', classmates)

print('len(classmates) =', len(classmates))

print('classmates[1] =', classmates[1])

print('classmates[-1] =', classmates[-1])

print(classmates.append('Alert'), classmates)

print(classmates.insert(2,'Bella'), classmates)

print(classmates.pop(), classmates)

#list 内容可以不一致
classmates[3] = 100
print(classmates)

subclassmates = ['zhuzhu', 'xiaoshandian']
classmates[2] = subclassmates
print(classmates)

print('len(classmates) =', len(classmates))


#tuple test
# the elements can not change
print()
print('tuple test...')
numbers = (1, 2, 3)
print(numbers)

new_num = (1)
print(new_num)

new_num2 = (1,)
print(new_num2)
print('len(new_num2) =',len(new_num2))

#if the element of tuple is list, you can change the list elemnet
#but you can not change tuple pointer