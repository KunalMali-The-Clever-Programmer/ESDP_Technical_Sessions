from library_package.lists import *
while True:
    print("----------------Menu--------------")
    print("1.reverse Number ")
    print("2.reverse of String Number ")
    print("0.exit ")
    
    ch=int(input("Enter the choice :  "))

    if ch==1:
        num=int(input("Enter the numbet to find reverse : "))
        print("reverse is ",reverse(num))
    elif ch==2:
        str=input("Enter the numbet to find reverse of String : ")
        print("reverse of String is ",rev_string(str))
    else:
        print("PLESEZ enter valid choise")