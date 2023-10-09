n=int(input("Enter the Number : "))
count=0
if(n==0 or num==1):
    print("the number is not prime")
for i in range(2,n):
    if(n%i==0):
        count=1
   
if(count==0):
    print("the number is prime ",n)
else:
    print("the number is not prime: ",n)