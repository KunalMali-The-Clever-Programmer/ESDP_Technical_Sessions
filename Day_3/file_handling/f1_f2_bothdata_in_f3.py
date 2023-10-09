f1=open("f1.txt","r+")
f2=open("f2.txt","r+")
f1.write("a \n")
f1.write("b \n")
f2.write("c \n")
f2.write("d \n")
f3=open("empty.txt","w")

a=f1.read()
b=f2.read()
data=f3.writelines(a+b)

print(data)
