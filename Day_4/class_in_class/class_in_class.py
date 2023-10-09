class student:
    def __init__(self,name,roll_no,sal):
        self.name=name
        self.roll_no=roll_no
        self.sal=sal
    def show(self):
        print("Name of the student is : ",self.name)
        print("Roll number of student is :",self.roll_no)
        print("Salary is : ",self.sal)

class test:
    def update(student):
        student.sal=student.sal+1000
        student.show()
e=student("kunal",21,12345)
e.show()
test.update(e)