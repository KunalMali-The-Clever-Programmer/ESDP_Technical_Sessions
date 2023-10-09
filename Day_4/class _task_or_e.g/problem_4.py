
class call_bill:
    def __init__(self,name,address,tel_no,no_call):
        self.name=name
        self.address=address
        self.tel_no=tel_no
        self.no_call=no_call
        
        
    def display(self):
        ch=self.no_call*2
        print("Name of the user : ",self.name)
        print("Address of the user : ",self.address)
        print("Tel Phone number of the user : ",self.tel_no)
        print("Number of Call of the user : ",self.no_call)
        print("Tatol Amount of all call Charges : ",ch)
        
name=input("Enter the Name : ")
address=input("Enter the address : ")
tel_no=int(input("Enter the Tel Phone number : "))
no_call=int(input("Enter the number of call: "))
a=call_bill(name,address,tel_no,no_call)
a.display()