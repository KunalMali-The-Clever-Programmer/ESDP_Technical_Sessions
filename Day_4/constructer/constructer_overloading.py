class con:
    def __init__(self):
        print("NO argument method.")
    def __init__(self,a):
        print("With one argrment .",a)
    def __init__(self,a,b):
        print("With Two argument .",(a+b))
obj=con()
obj.con(10)
obj.con(10,20)


#Error is occuer because constructer overloading is occuer we can perform by None value assing to the variable 