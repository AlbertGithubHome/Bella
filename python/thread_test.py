# thread test

import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 3:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


# Lock test

import time, threading

money = 0

def change_it(n):
    global money
    money = money + n
    money = money - n

def run_thread(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))

t1.start()
t2.start()

t1.join()
t2.join()

print('money = ', money)


# use Lock
money = 0
lock = threading.Lock()

def run_thread2(n):
    for i in range(1000000):

        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target = run_thread2, args = (5,))
t2 = threading.Thread(target = run_thread2, args = (8,))

t1.start()
t2.start()

t1.join()
t2.join()
print('money = ', money)
