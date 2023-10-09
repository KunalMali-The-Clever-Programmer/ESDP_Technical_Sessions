
def sum_series(st,end):
    sum=0
    while(st<=end):
        sum=sum+st
        st+=1
    return sum
        


st=int(input("Enter the starting number of sries : "))
sum=0
i=1
end=int(input("Enter the ending number of sries : "))
print("ans : ",sum_series(st,end))