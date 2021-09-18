'''
class player():
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def order(self):
        print(f"my name is {self.name}")
    @classmethod
    def ad(cls,num1,num2):
        return num1+num2
    @staticmethod
    def ad1(num3,num4):
        return num3+num4
p1 = player("dini",20)
#print(p1.order())
print(p1.ad1(20,30))
print(p1.ad(10,10))
'''


'''
s = {1, 2, 3, 4, 5, 6}
s.update("we")
print(s)

print(dir(s))
'''


'''
a = [1, 4, 5, 6, 7, 2, 8]
print(a)

"""
a[0] = a[1]
a[1] = a[2]
a[2] = a[3]
a[3] = a[4]
a[4] = a[5]
a[5] = a[6]
a[6] = 1
"""

test_list = a[1:] + a[0:1]
print(test_list)
'''
