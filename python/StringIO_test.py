# StringIO test

from io import StringIO

string_content = StringIO()

string_content.write("I'm ")
string_content.write("a ")
string_content.write("boy!")

print("string_content = ", string_content.getvalue())


string_content = StringIO('This is a test\nHello World!\nOK')
while True:
    line = string_content.readline()
    if line == '':
        break
    print(line.strip())

