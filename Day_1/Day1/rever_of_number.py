num=int(input("Enter the Three digit Number : "))
sum=0
rem=0
while(num!=0):
    rem=num%10
    #rem=rem*rem*rem
    sum=sum*10+rem
    num//=10
    print(sum)


print(f"Reveser of Number {num} :  ",sum)