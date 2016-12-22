# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

def start_worker():
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    server_addr = '127.0.0.1'
    print('Connect to server %s...', server_addr)

    #keep config same as server
    m = QueueManager(address = (server_addr, 5000), authkey = b'abc')

    # connect
    m.connect()

    # get queue
    task = m.get_task_queue()
    result = m.get_result_queue()

    for i in range(10):
        try:
            n = task.get(timeout = 10)
            print('run task %d * %d...' % (n , n))
            r = '%d * %d = %d' % (n , n, n * n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty.')
    print('worker exit.')

if __name__ == '__main__':
    start_worker()