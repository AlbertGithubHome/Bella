# type test

print('type(123) =', type(123))

print('type(abs) =', type(abs))

print('type(123) == int =', type(456) == int)

import types

def myadd(x, y):
    return x + y

print(type(myadd) == types.FunctionType) 


print(type(lambda x: x) == types.FunctionType) 
print(type(lambda x: x) == types.LambdaType) 

print(type(myadd) == types.LambdaType) 
print(type(myadd) == types.BuiltinFunctionType) 
