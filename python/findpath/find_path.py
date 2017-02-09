# find path
import base64, functools

# read source file content
with open('v.txt', 'r') as file_handle:
    content = file_handle.read().split()

with open('a.txt', 'r') as file_handle:
    a_content = file_handle.read().split()

#print(content)

pre_num = 0.0

L = []
La = []
count = 0
index = 0
cnt = 0
for num in content:
    cur_num = float(num)
    if abs(cur_num - pre_num) > 6:
        pre_num = cur_num
        count = count + 1
        index = cnt
    L.append(str(pre_num))
    La.append(a_content[index])
    cnt = cnt + 1

result = '\n'.join(La)
print(result)
print(count)

