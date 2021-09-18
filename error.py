while True:
    try:
        age = int(input("what is your age : "))
        print(10/age)
    except ValueError:
        print("please enter a number")
    except ZeroDivisionError:
        print("please enter age more than 0")
    else:
        print("Thank You")
        break
    finally:
        print("ok!!!!")






