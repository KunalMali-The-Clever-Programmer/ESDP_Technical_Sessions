class mypython:
    def sum(self , * n):
        tatol=0
        for x in n:
            tatol+=x

        print("Sum: ",tatol)

m=mypython()
m.sum(10,20)
m.sum(10,20,30)
m.sum(10)
m.sum()