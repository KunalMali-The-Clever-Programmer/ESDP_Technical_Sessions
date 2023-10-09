import math
class sphere:
    def __init__(self,r):
        self.r=r
    def display(self):
        s_a=4*math.pi*self.r*self.r
        print("Surface Area of sphere: ",s_a)
        v_s=4/3 *math.pi *self.r*self.r * self.r
        print("volume of sphere is : ",v_s)
r=int(input("Enter the redius of sphere is : "))
a=sphere(r)
a.display()