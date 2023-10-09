class tooyoungexception(Exception):
    def __init__(self, arg):
        self.msg = arg

class tooyoungexception(Exception):
    def __init__(self, arg):
        self.msg = arg

age= int(input("Enter your age : "))

if age >60:
    raise tooyoungexception("Wait some time  we will find best match for you : ")
elif age<18:
    raise tooyoungexception("You are not eligiable for marray")
else:
    print("You are eligiable for marray")



