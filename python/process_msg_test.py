# process communicate test

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to Queue ...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from Queue.' % value)

if __name__ == '__main__':

    q = Queue()
    pw = Process(target = write, args =(q,))
    pr = Process(target = read, args =(q,))

    # start write
    pw.start()

    # start read
    pr.start()

    # wait end
    pw.join()

    # terminate
    pr.terminate()

