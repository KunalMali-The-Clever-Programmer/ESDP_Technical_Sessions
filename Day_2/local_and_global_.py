a=10
print(a)
def local():
    b=20
    print("local variable",b)
    print("global variable ", a)
print("Globla ", a)
print("local ", local())
