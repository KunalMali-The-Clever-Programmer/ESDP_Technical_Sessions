n=int(input("Enter the  range to add even and odd  : "))
even=0
odd=0
for i in range(0,n):
    if(i%2==0):
        even=i
    if(i%2!=0):
        odd=i
    print(even+odd)