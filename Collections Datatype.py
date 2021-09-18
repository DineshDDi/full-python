'''
from collections import namedtuple
a = namedtuple('courses', 'name, technology')
b = a('Developer', 'python')
c = a._make(['artificial intelligence','python'])
print(b)
print(c)
'''


'''
from collections import deque
a = ['d','i','n','e','s','h']
d = deque(a)
print(d)

d.append('di')
print(d)

d.appendleft('di')
print(d)

d.pop()
print(d)
'''


'''
from collections import ChainMap
joining 2 dictionary using Chainmap keywords
'''

'''
from collections  import Counter
a = [1,2,3,4,5,6,1,2,2,1,2,3,4]
c = Counter(a)
print(c)
print(list(c.elements()))
s = {c.subtract}
'''

#counting a duplicate data's in index views  (element change list types   datatypename.elements its one function of counter)
#counting use also (most_common keywords,subtract  keywords)

'''
from collections import OrderedDict
d = OrderedDict()
d[1] = 'd'
d[2] = 'i'
d[3] = 'n'
d[4] = 'e'
d[5] = 's'
d[6] = 'h'
print(d)
'''

'''
from collections import UserDict
d = {'a': 1, 'b': 2, 'c': 3}

User = UserDict(d)
print(User.data)

User = UserDict()
print(User)
'''


'''
from collections import UserList

d = [1,2,3,4,5]

User = UserList(d)

print(User)

User.append(6)
print(User)
'''


'''
from collections import UserString
a = 12345

User = UserString(a)
print(a)
'''

#append and remove keys are accept in UserString





