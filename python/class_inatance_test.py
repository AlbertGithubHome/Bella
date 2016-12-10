# class and instance test

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' %(self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

dude = Student('Albert', 100)
dude.print_score()

print('Student =', Student)
print('dude =', dude)

print('dude.grade =', dude.get_grade())

print(dude.name)
dude.age = 8
print(dude.age)