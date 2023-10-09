try:
    a=int(input("Enter the value a : "))
    b=int(input("Enter the value b : "))
    print(a/b)
except ZeroDivisionError :
    print("You can't divsion by zero")
except:
    print("Defaual exception : Please enter vali input : ")