# hashlib test

import hashlib

mydigest = hashlib.md5()
mydigest.update('how to use md5 in python hashlib?'.encode('utf_8'))
print(mydigest.hexdigest())

print()
mydigest = hashlib.md5()
mydigest.update('1'.encode('utf_8'))
print(mydigest.hexdigest())
mydigest = hashlib.md5()
mydigest.update('2'.encode('utf_8'))
print(mydigest.hexdigest())
mydigest = hashlib.md5()
mydigest.update('3'.encode('utf_8'))
print(mydigest.hexdigest())
mydigest = hashlib.md5()
mydigest.update('4'.encode('utf_8'))
print(mydigest.hexdigest())
mydigest = hashlib.md5()
mydigest.update('5'.encode('utf_8'))
print(mydigest.hexdigest())

print()
mydigest = hashlib.md5()
mydigest.update(''.encode('utf_8'))
print(mydigest.hexdigest())

print()
mydigest = hashlib.md5()
mydigest.update('123456'.encode('utf_8'))
print(mydigest.hexdigest())

print()
new_digest = hashlib.sha1()
new_digest.update('how to use md5 in python hashlib?'.encode('utf_8'))
print(new_digest.hexdigest())

