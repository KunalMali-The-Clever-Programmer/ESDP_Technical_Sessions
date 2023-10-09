class mypython:
    x=10
    def __init__(self):
        self.y=20
    def show(self):
        print(x)
    

m1=mypython()
m2=mypython()
print("M1--->",m1.x,m1.y)
print("M2--->",m2.x,m2.y)
mypython.x=111
m1.y=222
print("m1--->",m1.x,m1.y)
print("M2--->",m2.x,m2.y)