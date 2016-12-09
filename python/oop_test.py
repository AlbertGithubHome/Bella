# oop——Object Oriented Programming

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' %(self.name, self.score))

aa = Student('Albert', 100)
aa.print_score()

bb = Student('Bella', 99)
bb.print_score()