def reverse(num):
    sum=0
    rem=0
    while(num!=0):
        rem=num%10
        sum=sum*10+rem
        num//=10
    return sum
def rev_string(str):
    rev=str[::-1]
    return rev