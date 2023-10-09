# num=int(input("Enter the number "))
# count=0
# rem=0
# while(num !=0):
#     rem=num%10
#     count+=1
#     num//=10
# if(count ==10):
#     print("the number is valid  or contain 10 digits")
# else:
#     print("the number is not  valid  or not contain 10 digits")

num=input("Enter the number ")
if len(num)==10 and num.isdigit():
    print("corrct")
else:
    print("false")
