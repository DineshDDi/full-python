'''
class square:
    def __init__(self, side):
        self._side = side
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self, value):
        if value >= 0:
            self._side = value
        else:
            print("error")
    @property
    def area(self):
        return self._side **2
    @classmethod
    def unit_square(cls):
        return cls(1)

a = square(5)
print(a.side)
print(a.area)
'''

'''
def d(func):
    def inner():
        print("this is inner function")
        func()
        print("this is outer function")
    return inner()

def r():
    print("this is 2nd function")

d(r)
'''

'''
def my_decorater(func):
    def wrap_func():
        print("*******")
        func()
        print("*******")
    return wrap_func

@my_decorater
def hello():
    print("Hellllooooo")

#a = my_decorater(hello)
#a()

hello()

'''


