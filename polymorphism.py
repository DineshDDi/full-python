class add:
    def calculation(self,a,b):
        self.a = a
        self.b = b
        return (a+b)
class sub:
    def calculation(self,a,b):
        self.a = a
        self.b = b
        return (a-b)
class div:
    def calculation(self,a,b):
        self.a = a
        self.b = b
        return (a/b)
class mul:
    def calculation(self,a,b):
        self.a = a
        self.b = b
        return (a*b)


a = add()
b = sub()
c = div()
d = mul()
print(b.calculation(45,10))












