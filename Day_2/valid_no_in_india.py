
# mob=int(input("Enter the mob number: "))
# ans=mob//10000000000
# if(ans==91):
#     print("true")
# else:
#     print("false")


mob=int(input("Enter the mob number: "))
m1=str(mob)
count=len(m1)
if m1.isdigit():
    if m1.startswith("91"):
        print("Valid moblie number : ")
    if(count==12):
        print("corrct mobile number: ")
    else:
        print("Invalid mobile number pleze enter corrct mobile no ....")





