str=input("Enter the string : ")  #kunal  
rev=""
for i in str:
    rev=i+rev
   # print("Reverse of String : ", rev)
#print("Reverse of String : ", rev)
if(str==rev):
    print("Palindrone string")
else:
    print("not a Palindrone string")