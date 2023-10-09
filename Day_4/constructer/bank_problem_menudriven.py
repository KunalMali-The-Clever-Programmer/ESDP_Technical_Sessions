import random
class bank:
    def __init__(self,name,add,ty_ac,ac_no,ini_bal):
        self.name=name
        self.add=add
        self.ty_ac=ty_ac
        self.ac_no=ac_no
        self.ini_bal=ini_bal
    def ini_bal1(self):
        print("Your iniaal balance in account is: ",self.ini_bal)
    def deposite(self):
        dep=int(input("Enter the amount to deposite :  "))
        self.ini_bal=self.ini_bal+dep
        print("Deposite Sucsefully........")
    def withdrow(self):
        withd=int(input("Enter the amount to withdraw:  "))
        if(withd>self.ini_bal):
            print("Insuffcient Balance")
        else:
            self.ini_bal=self.ini_bal-withd
            print("Withdrew Suceesfull..........")
        
    def display(self):
        print("User name : ",self.name)
        print("user address is :",self.add)
        print("Account types  :", self.ty_ac)
        print("User Acount number is : ",self.ac_no)
        print("Current balace in account is  :",self.ini_bal)
            



print("================================Welcome to bank of paradase================================")
name=input("Enter the Name of User : ")
add=input("Enter the Address of User : ")
ty_ac=input("Enter the type of acount to create : ")
print("Account create succfully ")
    
minimum = pow(10, 10-1)
maximum = pow(10, 10) - 1
ac_no= random.randint(minimum, maximum)
print("Your acount number is ",ac_no)
ini_bal=int(input("Enter the initail balace in account: "))
a=bank(name,add,ty_ac,ac_no,ini_bal)

while True:
    print("----------------Menu--------------")
    print("1.Initial Balance  ")
    print("2.Deposite ")
    print("3.Withdraw ")
    print("4.Account Information")
    ch=int(input("Enter the choice :  "))

    if ch==1:
        print(a.ini_bal1())
    elif ch==2:
         print(a.deposite())
    elif ch==3:
        print(a.withdrow())
    elif ch==4:
        print(a.display())
    