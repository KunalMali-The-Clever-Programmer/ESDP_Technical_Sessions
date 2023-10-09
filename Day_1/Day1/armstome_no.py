n=int(input("Enter the Three digit Number : "))
num=n
sum=0
rem=0
while(num!=0):
    rem=num%10
    #rem=rem*rem*rem
    sum=sum+rem**3
    num//=10
    print(sum)
if(sum ==n):
    print("number is armstome ")
else:
    print("number is not  armstome ")
# def arm(num):
#     sum=0
#     rem=0
#     while(num!=0):
#         rem=num%10
#         #rem=rem*rem*rem
#         sum+=rem*rem*rem
#         num//=10
#         print(sum)
#     if(sum==num):
#         return True
#     else:
#         return False
    
# print(arm(num))
