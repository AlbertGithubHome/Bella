#__slots__ test

class Student(object):
    pass

s = Student()
s.name = 'Albert'
print(s.name)


def set_age(self, age):
    self.age = age

from types import MethodType

# Add a function to Object s
s.set_age = MethodType(set_age, s)
s.set_age(20)
print(s.age)


class Teacher(object):
    __slots__ = ('name', 'sex', 'set_age')

t = Teacher()
t.name = 'XiaoMing'
print(t.name)

#Error, Because of __slots__
#AttributeError: 'Teacher' object has no attribute 'score'
#t.age = 12
#print(t.age)

Teacher.set_age = MethodType(set_age, Teacher)
t.set_age(20)
print(t.age)
#
#
#
#Thank you for this example
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000 #2
def set_city(self, city):
    self.city=city

class Student2(object):
    __slots__ = ('name', 'age', 'set_city')
    pass

Student2.set_city = MethodType(set_city, Student2)

a = Student2()
a.set_city('Beijing')
print(a.city)