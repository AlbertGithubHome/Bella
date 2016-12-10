# inherit test

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    pass

dog = Dog()
dog.run()

a = list()
b = Animal()
c = Dog()


print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(b, Dog))
print(isinstance(c, Animal))
print(isinstance(c, Dog))

def run_twice(animal):
    animal.run()
    animal.run()


# like duck type
run_twice(b)
run_twice(c)