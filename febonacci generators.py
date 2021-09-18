def new():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
for x in new():
    if x>50:
        break
    print(x, end=" ")


'''
a = [1,2,3]
b= [a[0]*2,a[1]*2,a[2]*2]
print(b)
'''



