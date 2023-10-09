class parent:
    def propertice(self):
        print("In the parent class ...")
class chiled:
    def pro(self):
        print("In the child ... ")
class multiple(parent,chiled):
    def multiple_method(self):
        print("In the multilevel..")
object=multiple()
object.multiple_method()
object.propertice()
object.pro()
