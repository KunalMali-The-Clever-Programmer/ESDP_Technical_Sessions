"""
n=int(input("Enter the  Number : "))
last_number=n%10
while(n!=0):
    rem=n%10
    n//=10
    if(n==0):
        first=rem
print(first+last_number)

"""
#in two steps 
no=int(input("Enter the  Number : "))
n1=no%10
n2=no//100000000
print(n1+n2)
