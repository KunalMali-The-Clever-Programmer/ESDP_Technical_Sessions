set1={10,20,30,30,50}
print(set1)
set1.add(100)
print(set1)

set2=set1.copy()
print(set2)
set1.remove(100)
print(set1)
print(set2.clear())
set3={1,2,3,4}
# del set3
print(set3)

l=eval(input("Enter the list: "))
set7=set(l)
print(set7)