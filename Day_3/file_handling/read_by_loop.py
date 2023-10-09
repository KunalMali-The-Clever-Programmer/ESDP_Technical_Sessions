f=open("abc.txt",'r')
l1= f.readline()
for i in l1:
    print(i, end=" ")
f.close()
