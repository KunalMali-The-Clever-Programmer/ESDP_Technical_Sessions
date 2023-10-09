num=int(input("Enter the 1 number ; "))
num2=int(input("Enter the 2 number ; "))
num3=int(input("Enter the 3  number ; "))

if(num >num2 and num >num3):
    print(f"{num} greater than other numbers ")
elif(num2 >num and num2 >num3):
    print(f"{num2} greater than other numbers ")
else:
    print(f"{num3} greater than other numbers ")