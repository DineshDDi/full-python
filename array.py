from array import *

a = array('d', [1, 2, 3, 4, 5, 6, 7, 8, 9])
a.append(10)
print(a)

a.extend([11,17])
print(a)

a.insert(11, 12)
print(a)

a.pop(11)
print(a)

a.remove(11)
print(a)

b = array('d', [11,12,13,14])
c = array('d')
c = a+b
print(c)



