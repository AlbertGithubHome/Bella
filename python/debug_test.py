# debug test

def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

#main()


def foo2(s):
    n = int(s)
    assert n != 0,'n is zero!'
    return 10 / n

def main2():
    foo2('0')


#main2()


import logging
logging.basicConfig(level=logging.INFO)

n = 0
logging.info('n = %d' % n)
#print(10 / n)


#print
#assert
#logging
#pdb
#pdb.set_trace()