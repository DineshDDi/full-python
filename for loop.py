'''
num = int(input("Number:"))
dd = 1
if num < 0:
    print("must be positive")
elif num == 0:
    print("dd=1")
else:o
    for w in range(1, num+1):
        dd = dd*w
print(dd)
'''

'''
for num in range(1,100):
    for w in range(2,num):
        if num%w==0:
            print(num, "is not a prime number")
            break
    else:
        print(num,"is prime number")
'''

'''
num = int(input("numbers : "))
count = 0
for w in range (1,num):
    if num%w == 0:
        count += 1
if count == 1:
    print(num,"is prime number")
else :
    print(num,"is not prime number")
'''

'''
a = 2
while a < 100:
    for b in range(2, a):
        if a%b==0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is prime number")
    a += 1
'''


'''
a = int(input("Numbers : "))
d = 1
for x in range(1, a+1):
    d = d*x
print(d)
'''



