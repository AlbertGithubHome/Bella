# serialization test


# pickle module
import pickle

d = dict(name = 'Albert', age = 18, score = 100)
dump_ret = pickle.dumps(d)
print('dump_ret =', dump_ret)

with open('dump.txt', 'wb') as file:
    pickle.dump(d, file)

with open('dump.txt', 'rb') as file_w:
    new_d = pickle.load(file_w)

print('new_d =', new_d)

# json moudle
import json
json_string = json.dumps(d)
print('json_string =', json_string)

new_dd = json.loads(json_string)
print('new_dd =', new_dd)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Albert', 18, 99)
print('s =', s)

# TypeError: <__main__.Student object at 0x00684570> is not JSON serializable
#json_student = json.dumps(s)


def student2dict(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }

json_student = json.dumps(s, default=student2dict)
print('json_student =', json_student)

json_student2 = json.dumps(s, default=lambda obj:obj.__dict__)
print('json_student2 =', json_student2)

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(json_student2, object_hook=dict2student))