class parent:
    def propertice(self):
        print("In the parent class ...")
class chiled(parent):
    def pro(self):
        print("In the child ... ")
class hirachical(parent):
    def hirachical_method(self):
        print("In the hirachical ..")
object=hirachical()
object.hirachical_method()
object.propertice()

