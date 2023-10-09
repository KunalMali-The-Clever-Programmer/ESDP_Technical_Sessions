try:
    a=int(input("Enter the value a : "))
    b=int(input("Enter the value b : "))
    print(a/b)
except (ZeroDivisionError,ValueError) as msg:
    print("plesez enter the valid input : ",msg)
