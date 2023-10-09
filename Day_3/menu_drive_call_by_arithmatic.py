import Aritmatic as a

while True:
    print("----------------Menu--------------")
    print("1.Armstong Number ")
    print("2.Palindome Number ")
    print("3.factorial Number ")
    print("4.reverse Number ")
    ch=int(input("Enter the choice :  "))

    if ch==1:
        num=int(input("Enter the numbet to find armstong  or not : "))
        print("armstome is ",a.arm(num))
    elif ch==2:
        num=int(input("Enter the numbet to find Palindome  or not : "))
        print("Palindome is ",a.pali(num))
    elif ch==3:
        num=int(input("Enter the numbet to find factorial  or not : "))
        print("factorial is ",a.fact(num))
    elif ch==4:
        num=int(input("Enter the numbet to find reverse  or not : "))
        print("reverse is ",a.reverse(num))
    
