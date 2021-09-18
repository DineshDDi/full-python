#import thread
'''
import time

for x in range(0,5):
    print(x)
'''


def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0

res = calculateSum(10)
print(res)



