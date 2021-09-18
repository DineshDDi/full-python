'''
def s(r):
    k = r
    for d in range(r, -1, -1):
        for e in range(k, 0, -1):
            print(end=" ")
        k = k+1
        for e in range(0, d+1):
            print("* ",end="")
        print("\r")
s(4)
'''

'''
def s(r):
    k = r
    for d in range(0, r+1):
        #for e in range(0, k):
            #print(end=" ")
            #k = k-1
        for e in range(0, d+1):
             print("* ",end="")
        print("\r")
s(4)
'''

'''
def a(n):
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k-2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
a(4)
'''

'''
def s(r):
    k = 2*r-2
    for i in range(0,r):
        for j in range(0,k):
            print(end=" ")
        k = k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
s(5)
'''


'''
def s(r):
    for d in range(0, r+1):
        for e in range(0, d+1):
            print("* ", end="")
        print("\r")
    for d in range(r,-1,-1):
        for e in range(1,d+1):
            print("* ",end="")
        print("\r")
s(4)
'''





