def divi(n):
    a = 0
    for i in range(0, n):
        a = a+1
        for v in range(0, i+1):
            print(a, end=" ")
        print(" ")

divi(10)


