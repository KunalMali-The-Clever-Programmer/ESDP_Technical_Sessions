class student:
    def __init__(self,name,roll_no,add,per):
        self.name=name
        self.roll_no=roll_no
        self.add=add
        self.per=per
    def viwe_info(self):
        print("Student name is :",self.name)
        print("Student Roll Number is :",self.roll_no)
        print("Student Address is :",self.add)
        print("Student Percentage is :",self.per)
    def gread_info(self):
        if(self.per>=70):
            print("Student pass with DISTINCTION.....")
        elif(self.per<70 and self.per>=60):
            print("Stuent Pass with FIRST CLASS....")
        elif(self.per<60 and self.per>=40):
            print("Student pass with SECOND CLASS.....")
        else:
            print("Student is fail...")



print("================================Welcome to RCPIT================================")
name=input("Enter the Name of User : ")
roll_no=input("Enter the Roll Number : ")
add=input("Enter the Address of User : ")
per=int(input("Enter the Percentages : "))
print("Thanks for Information ...... ")
a=student(name,roll_no,add,per)

while True:
    print("----------------Menu--------------")
    print("1.view information ")
    print("2.Display info with grades  ")
    ch=int(input("Enter the choice :  "))

    if ch==1:
         print(a.viwe_info())
    elif ch==2:
        print(a.gread_info())
    