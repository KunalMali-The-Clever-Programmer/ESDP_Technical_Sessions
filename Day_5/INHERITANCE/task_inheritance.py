class emp:
    new_sal=0  
    def work(self):
        self.name="om"
        self.id=1
        self.work="Devloper"
        # print("============Before Update Information===================")
        # print("Name of the employee is : ",self.name)
        # print("ID of the employee is : ",self.id)
        # print("Work of the employee is : ",self.work)
    
    def get_salary(self):
        self.sal_emp=0
        # print("Salary of the employee is : ",self.sal_emp)
    

class HR_manager(emp):
 
    def work(self):
        work="Hireing new employees "
        super().work()
        print(work)
    def add_new_detalid_emp(emp):
        print("============current Information===================")
        print("Name of the employee is : ",emp.name)
        print("ID of the employee is : ",emp.id)
        print("Work of the employee is : ",emp.work)
        # print("New Salary is : ",emp.sal_emp)
        # print("Salary of the employee is : ",emp.sal_emp)
        emp.name=input("Add new Name : ")
        emp.id=input("Add new ID :")
        emp.work=input("Enter new work :")
        emp.new_sal=int(input("Enter to add new salary: "))
        # emp.sal_emp=new_sal
        # print("New Salary is : ",new_sal)
    def display(emp):
    
        print("===========Updated information=====================")
        print("Name of the employee is : ",emp.name)
        print("ID of the employee is : ",emp.id)
        print("Work of the employee is : ",emp.work)
        print("New Salary is : ",emp.new_sal)
        
obj=HR_manager()

obj.work()
obj.add_new_detalid_emp()
# obj.get_salary()
# obj1=emp()
# obj1.work()
# obj1.get_salary()
obj.display()

