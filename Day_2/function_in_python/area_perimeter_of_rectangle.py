def area_rec(l,b):
    res=l*b
    return res
l=int(input("Enter the length of reacgle"))
b=int(input("Enter the breath of reacgle"))
print("area Of Ractagle is : ",area_rec(l,b))

def per_rec(l,b):
    res=2*(l+b)
    return res

l=int(input("Enter the length of reacgle"))
b=int(input("Enter the breath of reacgle"))
print("perimeter Of Ractagle is : ",per_rec(l,b))