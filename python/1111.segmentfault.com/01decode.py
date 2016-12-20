# import necessary package
import base64, functools

# read source file content
with open('01string.txt', 'r') as file_handle:
    content = file_handle.read().replace('_', '1').split()

# decode with base64 and output result into a file of 'tar.gz' type
with open('1111.segmentfault.com.tar.gz', 'wb') as file_handle:
    file_handle.write(base64.b64decode(functools.reduce(lambda x, y : x + y, map(lambda n : chr(int(n, base=2)), content))))