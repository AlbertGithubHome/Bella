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
pre_v = 0
for num in a_content:
    cur_num = float(num)
    if abs(cur_num - pre_num) > 1:
        pre_num = cur_num
        count = count + 1
        index = cnt
        L.append(content[index])
        pre_v = float(content[index])
    else:
        L.append(str(pre_v + pre_num))
        pre_v = pre_v + pre_num

    La.append(str(pre_num))
    cnt = cnt + 1

result = '\n'.join(L)
print(result)
print(count)

