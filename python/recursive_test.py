#recursive test
#from function_test import myabs

def fact(x):
    if x == 1:
        return x;
    return x * fact(x - 1)

print('fact(5) =', fact(5))

print('fact(200) =', fact(200))

'''
fact(200) = 78865786736479050355236321393218506229513597768717326329474253324435944996340334292030428401198462390417
13891963883025764279024263710506192662495282993111346285727076331723739698894392244562145166424025403329186413122742
85327752424240757390324032125740557956866022603190417032406235170085879617892222278962370389737472000000000000000000
000000000000000000000000000
'''

def fact_start(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# tail recursive invalid
# print('fact_start(1000) =', fact_start(1000))
'''
...
  File "recursive_test.py", line 26, in fact_iter
    return fact_iter(num - 1, num * product)
  File "recursive_test.py", line 26, in fact_iter
    return fact_iter(num - 1, num * product)
  File "recursive_test.py", line 24, in fact_iter
    if num == 1:
RuntimeError: maximum recursion depth exceeded in comparison
'''
