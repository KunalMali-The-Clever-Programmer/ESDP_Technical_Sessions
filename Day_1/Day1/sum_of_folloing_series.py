'''
series :-

sum=1+x/1 +x^2/2  + x^3/3 +.........x^n/n
'''
sum=1
n=int(input("Enter the range: "))
x=int(input("Enter the value of x : "))
for i in range(1,n+1):
    sum=sum+((x**i)/i)
print(sum)
