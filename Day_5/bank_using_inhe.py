import random
class bank:
    def __init__(self):
        self.name="name"
        self.add="add"
        # self.ty_ac=ty_ac
        self.ac_no=1233455353
        self.ini_bal=2000
    # def ini_bal1(self):
    #     print("Your iniaal balance in account is: ",self.ini_bal)
    def deposite(self):
        dep=int(input("Enter the amount to deposite :  "))
        self.ini_bal=self.ini_bal+dep
        print("Deposite Sucsefully........")
    def withdrow(self):
        # withd=int(input("Enter the amount to withdraw:  "))
        if(self.ini_bal<0):
            print("Insuffcient Balance")
        else:
            print("Note:  inital balance below than 1000 please maintein greatre than 1000  balance........")
        
    def display(self):
        print("User name : ",self.name)
        print("user address is :",self.add)
        # print("Account types  :", self.ty_ac)
        print("User Acount number is : ",self.ac_no)
        print("Current balace in account is  :",self.ini_bal)
            


class saving_account(bank):

    # print("================================Welcome to bank of paradase================================")
    # name=input("Enter the Name of User : ")
    # add=input("Enter the Address of User : ")
    #         # ty_ac=input("Enter the type of acount to create : ")
    # print("Account create succfully ")
                
    # minimum = pow(10, 10-1)
    # maximum = pow(10, 10) - 1
    # ac_no= random.randint(minimum, maximum)
    # print("Your acount number is ",ac_no)
    # ini_bal=int(input("Enter the initail balace in account: "))
    # a=bank(name,add,ac_no,ini_bal)
    def withdrow(self):
        withd=int(input("Enter the amount to withdraw:  "))
        if(self.ini_bal>=1000 and withd<=self.ini_bal):
            self.ini_bal = self.ini_bal-withd
            print("Withdrew Suceesfull..........")
        else:
            return super().withdrow()
obj=saving_account()
while True:
    print("----------------Menu--------------")
        # print("1.Initial Balance  ")
    print("1.Deposite ")
    print("2.Withdraw ")
    print("3.Account Information")
    ch=int(input("Enter the choice :  "))

    if ch==1:
         print(obj.deposite())
    elif ch==2:
        print(obj.withdrow())
    elif ch==3:
        print(obj.display())

