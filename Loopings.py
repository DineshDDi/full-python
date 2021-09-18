
import random
a = 10
b = int(a*random.random())+1
c = 0
while c != b:
    c = int(input("New Number: "))
    if c > 0:
        if c > b:
            print("Number too large")
        elif c < b:
            print("Number too short")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("congratulation. You made it!")



'''

import random

b = 10
a = int(b*random.random())+1

print(a)
'''





