
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)



with open('example_ret.txt', 'w') as file:
    file.write('Hello, Wolrd!')


#attempt has failed