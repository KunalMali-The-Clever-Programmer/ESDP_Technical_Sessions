class public:
    def __init__(self):
        self.public_variable="Public variable"
    def show(self):
        print("Public method")
obj=public()
print(obj.public_variable)
print(obj.show())