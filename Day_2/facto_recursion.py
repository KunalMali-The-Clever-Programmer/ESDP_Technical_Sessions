def factorial(n):
    if n==0 or n==1:
        return 1
    fact=1
    fact=n*factorial(n-1)
    return fact
n = int(input("Enter the number to find factorial:  "))
print(f"Factorial of {n} is ",factorial(n))