class student:
    def setName(self,name):
        self.name=name

    def getname(self):
        return self.name

    def setper(self,per):
        self.per=per
    def getper(self):
        return self.per
    
n=int(input("Enter the no of student: "))
s=student()
for i in range(n):
    name=input("Enter the student name: ")
    s.setName(name)
    per=int(input("Enter the percentege : "))
    s.setper(per)
    print("HI",s.getname(),"YOur percenge is ",s.getper())
    print()