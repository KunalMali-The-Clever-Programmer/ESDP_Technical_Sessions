class private:
    def __init__(self):
        self.__private_variable="private variable"
    def __show(self):
        print("private method")
obj=private()
print(obj._private__private_variable)
print(obj._private__show())