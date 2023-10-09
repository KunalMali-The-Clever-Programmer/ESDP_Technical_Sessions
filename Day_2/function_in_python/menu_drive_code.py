import sys
def add(a,b):
    res=a+b
    return res

def sub(a,b):
    res=a-b
    return res

def mul(a,b):
    res=a*b
    return res

def div(a,b):
    res=a/b
    return res

def fact(n):
    f=1  
    for i in range(1,n+1):
        f*=i
    return f


def power(a,b):
    res=a**b
    return res

def rev(num):
    sum=0
    rem=0
    while(num!=0):
        rem=num%10
        sum=sum*10+rem
        num//=10
    return sum
def pali(num):
    n=num
    rem=0
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum*10+rem
        n=n//10
    if(sum==num):
        return True
    else:
        return False
     
def arm(num):
    sum=0
    rem=0
    while(num!=0):
        rem=num%10
   
        sum=sum+rem**3
        num//=10
    if(num==sum):
        return True
    else:
        return False
ch=0
while True:
    print("# Menu: #")
    print("1. Additon")
    print("2. substraction")
    print("3. multiplecation")
    print("4. division")
    print("5. factorial")
    print("6. power")
    print("7. reverse")
    print("8. palindrone")
    print("9. armtrong")
    print("10. exit")
    ch=int(input("Enter the Choice:"))
    
    if(ch==1):
        a=int(input("enter the value of number 1 : "))
        b=int(input("enter the value of number 2 : "))
        print("addition is ",add(a,b))
    elif(ch==2):
         a=int(input("enter the value of number 1 : "))
         b=int(input("enter the value of number 2 : "))
         print("susbtraction  is ",sub(a,b))
    elif(ch==3):
         a=int(input("enter the value of number 1 : "))
         b=int(input("enter the value of number 2 : "))
         print("multiplaction is  is ",mul(a,b))
    elif(ch==4):
         a=int(input("enter the value of number 1 : "))
         b=int(input("enter the value of number 2 : "))
         print("division  is ",div(a,b))
    elif(ch==5):
         n=int(input("enter the value of number 1 : "))
         
         print("factorial is ",fact(n))
    elif(ch==6):
         a=int(input("enter the value of number 1 : "))
         b=int(input("enter the value to be the power of number 1 : "))
         
         print("power is ",power(a,b))
    elif(ch==7):
         num=int(input("enter the number to reverse : "))
        #  b=int(input("enter the value to be the power of number 1 : "))
         
         print("reverse is ",rev(num))
    elif(ch==8):
         num=int(input("enter the number to check palindrone or not "))
        #  b=int(input("enter the value to be the power of number 1 : "))
         
         print("palindrone is ",pali(num))
    elif(ch==9):
         num=int(input("enter the number to check palindrone or not  : "))
        #  b=int(input("enter the value to be the power of number 1 : "))
         
         print("armstome is ",arm(num))
    else:
        print("plesez enter valid choice ....")


