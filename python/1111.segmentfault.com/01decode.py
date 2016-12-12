# import necessary package
import base64
from functools import reduce

# read source file content
file_handle = open('01string.txt', 'r')
content = file_handle.read().replace('_', '1').split()
file_handle.close()

# decode with base64
decode_content = reduce(lambda x, y : x + y, map(lambda n : chr(int(n, base=2)), content))
decode_content = base64.b64decode(decode_content)

# output result into a file of 'tar.gz' type
file_handle = open('1111.segmentfault.com.tar.gz', 'wb')
file_handle.write(decode_content)
file_handle.close()