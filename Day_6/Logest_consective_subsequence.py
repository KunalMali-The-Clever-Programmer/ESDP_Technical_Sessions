n = int(input("Enter the Number of numbers to add in Array: "))
list1 = []

for i in range(n):
    num = int(input("Enter the number: "))
    list1.append(num)

print("Your Array is:", list1)

list1.sort()
print(list1)

count = 1
ans = 1

for i in range(n - 1):
    if list1[i + 1] == list1[i] + 1:
        count += 1
        if count >= ans:
            ans = count
    else:
        count = 1

print(ans)
