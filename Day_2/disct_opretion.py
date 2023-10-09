d={'kunal':23,'om':24,'druv':25}
print(d)
d.clear()
print(d)
d1={}
d1['kunal']=10
d1['om']=30
d1['abc']=20
print(d1)

d1['xyz']=288
print(d1)

res={}
n=int(input("Enter the Number of Student: "))
i=1
while(i<n):
    name=input("Enter the name of student : ")
    marks =input("Enter the marks of student in % : ")
    res[name]=marks
    i+=1
print(res)
print("Name Of Student", "\t", "marks OF Student ")
for x in res.keys():
    print("\t",x ,"\t\t",res[x])

d4=dict({100:"k",200:"u" , 300:"n"})
print(d4)
d5=dict([(10,'a'),(20,'b'),(30,'c')])
print(d5)
print(d5.get(10))
print(d5.get(40,"cdf"))