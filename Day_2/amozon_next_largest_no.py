arr=[1,3,2,4]
for i in range(len(arr)):
    if(arr[i]<arr[i+1]):
        arr[i]=arr[i+1]
        print(arr[i])