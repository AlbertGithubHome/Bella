#file and dir test

import os

print('os.name =', os.name)

#There is not a uname() on Windows
#print('os.uname() =', os.uname())

print('os.environ =', os.environ)

print("os.environ.get('PATH') =", os.environ.get('PATH'))

current_path = os.path.abspath('.')
print('current_path =', current_path)

sub_path = os.path.join(current_path, 'subtest.txt')
print('sub_path =', sub_path)

split_ret = os.path.split('E:\GitProject\Bella\python')
print('split_ret =', split_ret)

split_ret = os.path.split(sub_path)
print('split_ret =', split_ret)

split_txt_ret = os.path.splitext(sub_path)
print('split_txt_ret =', split_txt_ret)

L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print('L = ', L)