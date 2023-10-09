# # Find Missing number in array N-1.....

no_elemnt=int(input("Enter the number of elemrnt is: "))

list1=[]
sum=0
no_elemnt1=no_elemnt-1
for i in range(no_elemnt1):
    num=int(input("Enter the number: "))
    list1.append(num)
    sum+=num
    no_elemnt1-=1
print(list1)
# print(sum)
total_sum = no_elemnt*(no_elemnt+1)//2  
ans = total_sum -sum

print("Missing Number is : ",ans)
