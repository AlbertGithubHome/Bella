# file test
# 
file_descriptor = open('enum_test.py', 'r')

#print(file_descriptor.read())

file_descriptor.close()


# show IOError

'''
try:
    f = open('haha.py', 'r')
    print(f.read())
finally:
    print('============')
    if f:
        f.close()
'''

#use with
with open('enum_test.py') as f:
    print(f.read())
