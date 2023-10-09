class parent:
    def Propertice(self):
        print("cash ","gold")

    def bike(self):
        print("BMW")
class child (parent):
    def bike(self):
        print("Laborgine")

c=child()
c.Propertice()
c.bike()