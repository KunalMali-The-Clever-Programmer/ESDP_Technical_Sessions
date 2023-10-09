from abc import ABC,abstractmethod
class Rcpit(ABC):
    @abstractmethod
    def student_detealis(self):
        pass
    
    @abstractmethod
    def student_Assignment(self):
        pass

    @abstractmethod
    def student_marks(self):
        pass
class comp_c(Rcpit):
    def student_detealis(self):
        return "It will return student Detealis of computer c"
    def student_Assignment(self):
        return "ITs will reutrn student assigenment of com c"
    def student_marks(self):
        return "It will providing detelas student_marks com c"
class data_sci(Rcpit):
    def student_detealis(self):
        return "IT reutrn the detaile of student_detealis of data science"
    def student_Assignment(self):
        return "ITs will reutrn student assigenment of data science"
    def student_marks(self):
        return "It will providing detelas student_marks data science"
ds=comp_c()
print(ds.student_detealis())
print(ds.student_Assignment())
print(ds.student_marks())