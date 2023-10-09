a=0
b=1
count=0
range=int(input("Enter the number to you want find upto fibonacci series : "))
while(count<range):
    nextterm=a+b
    a=b
    b=nextterm
    print(nextterm)
    count=count+1