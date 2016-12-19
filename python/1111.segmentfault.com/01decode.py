# import necessary package
import base64
from functools import reduce

# read source file content
with open('01string.txt', 'r') as file_handle:
    content = file_handle.read().replace('_', '1').split()

# decode with base64
decode_content = base64.b64decode(reduce(lambda x, y : x + y, map(lambda n : chr(int(n, base=2)), content)))

# output result into a file of 'tar.gz' type
with open('1111.segmentfault.com.tar.gz', 'wb') as file_handle:
    file_handle.write(decode_content)