def arm(num):
    sum=0
    rem=0
    while(num!=0):
        rem=num%10
        #rem=rem*rem*rem
        sum=sum+rem*rem*rem
        num//=10
        # print(sum)
    if(num==sum):
        print("number is armstome ")
    else:
        print("number is not  armstome ")
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
    
def fact(num):
    f=1  
    for i in range(1,num+1):
        f*=i
    return f

def reverse(num):
    sum=0
    rem=0
    while(num!=0):
        rem=num%10
        sum=sum*10+rem
        num//=10
    return sum