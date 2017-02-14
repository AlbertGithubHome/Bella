import re
print("little lightning tools:\n")

with open('source.txt', 'r') as file_handle:
	content = file_handle.read()

ret_list = re.findall(r'(?<=/">)(.+?)(?=</a></td>)', content)

#output result
for x in ret_list:
	print(x)