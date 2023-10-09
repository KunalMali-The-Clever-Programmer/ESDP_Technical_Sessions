"""num1=123
rem=0
sum=0
while(num1 !=0):
    rem=num1%10
    sum+=rem
    num1//=10
print(sum)
#print(num1+num2+num3)"""
num=int(input("Enter the number ; "))
num1=num%10         #123 ---3
n1=num//10        #12
num2=n1%10     #2
n2=n1//10
num3=n2%10
sum=num1+num2+num3
print(sum)



