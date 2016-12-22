#task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# send task queue
task_queue = queue.Queue()

# receive result queue
result_queue = queue.Queue()

# define queue manager
class QueueManager(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

def start_master():
    # register queue to network
    QueueManager.register('get_task_queue', callable = return_task_queue)
    QueueManager.register('get_result_queue', callable = return_result_queue)

    # bind port 5000
    manager = QueueManager(address = ('127.0.0.1', 5000), authkey = b'abc')

    # start queue
    manager.start()

    # get queue
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # input task
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # get result
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout = 30)
        print('Result: %s' % r)

    # close
    manager.shutdown()
    print('master exit.')


if __name__ == '__main__':
    start_master()