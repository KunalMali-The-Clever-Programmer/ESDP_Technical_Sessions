gender=input("Enter the gender (M/F)  ; ")
sub1=int(input("Enter the 1 subject ; "))
sub2=int(input("Enter the 2 subject ; "))
sub3=int(input("Enter the 3  subject ; "))

per=((sub1+sub2+sub3)/300)*100
if(gender=="m" and per>=62):
    print("welcome to RCPIT beacuse your admision in done ")
elif( gender=="f"or gender=="F" and per>=92 ):
    print("welcome to RCPIT beacuse your admision in done ")
else:
    print("Sorry your admision in not conform because your not colifoy percenter round..")


    

    

