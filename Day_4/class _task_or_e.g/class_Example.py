class student:
    def __init__ (self,name,age,per):
        self.name=name
        self.age=age
        self.per=per
    def info(self):
        print("\n Name of the user : ",self.name)
        print("\n age is of the user  : ",self.age)
        print("\n Percentage is : ",self.per)
name=input("Enter the name :")
age=int(input("Enter the age  :"))
per=int(input("Enter the percentage  :"))
s=student(name,age,per)
s.info()
