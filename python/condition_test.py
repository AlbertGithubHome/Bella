# condition test
if 55 > 32 :
    print("55 > 32 is", 55 > 32)
    
age = 20
print("age %d is " % age)
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
    
# condition test
# int funcion can convert string to int
bithday = input('birth: ')
birth = int(bithday)
if birth < 2000:
    print('00前')
else:
    print('00后')