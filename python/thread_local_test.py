# thread local test

import threading, time, random

local_school = threading.local()

def process_student():
    student_name = local_school.student
    time.sleep(random.random() * 3)
    print('Hello , %s (in %s)' % (student_name, threading.current_thread().name))

def process_thread(student_name):
    local_school.student = student_name
    process_student()

t1 = threading.Thread(target =process_thread, args = ('Albert',), name = 'Thread-A')
t2 = threading.Thread(target =process_thread, args = ('Bella',), name = 'Thread-B')

t1.start()
t2.start()

t1.join()
t2.join()