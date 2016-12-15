# customization test
# 
class Student(object):

    def __init__(self, name):
        self.name = name


    def __str__(self):
        return 'Student object (name : %s)' % self.name

    def __getattr__(self, attr):
        if attr == 'age':
            return 18

print(Student('Albert'))


