#Enum test

from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, "=>", member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print()
day1 = Weekday.Fri
print('day1 =', day1)

print(Weekday.Tue)
print(Weekday['Mon'])

print(Weekday.Fri == day1)

print()
for name, member in Weekday.__members__.items():
    print(name, "=>", member, ',', member.value)