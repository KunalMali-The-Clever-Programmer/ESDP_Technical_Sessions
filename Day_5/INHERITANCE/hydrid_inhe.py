class parent:
    def propertice(self):
        print("In the parent class ...")
class chiled(parent):
    def pro(self):
        print("In the child ... ")
class super_chid(parent):
    def super_chid_method(self):
        print("In the super_chid ... ")
class multiple(chiled,super_chid):
    def multiple_method(self):
        print("In the multiple..")
object=multiple()
object.multiple_method()
object.propertice()
object.pro()
object.super_chid_method()
