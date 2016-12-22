# collections test

# namedtuple
p = (1, 2)
print(p)

from collections import namedtuple

Point = namedtuple('MyPoint', ['x', 'y'])
p = Point(1, 3)
print(p)

print(isinstance(p , Point))
print(isinstance(p , tuple))

#deque
print()
from collections import deque

myque = deque(['x', '1','d' ])
myque.appendleft('c')
myque.appendleft('=')
print(myque)
myque.popleft()
print(myque)

#defaultdict
print()
from collections import defaultdict
myd = defaultdict(lambda: 'None')

myd['key1'] = 'abc'
myd['key2'] = 'abc'

print(myd['key1'])
print(myd['key2'])
print(myd['key3'])

#OrderedDict
print()
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

myContain = LastUpdatedOrderedDict(3)

myContain['x'] = 1
myContain['y'] = 1
myContain['z'] = 1
myContain['w'] = 1
myContain['w'] = 1
print(myContain)

#Counter
print()
from collections import Counter

c = Counter()
for n in 'I love code':
    c[n] = c[n] + 1

print(c)
