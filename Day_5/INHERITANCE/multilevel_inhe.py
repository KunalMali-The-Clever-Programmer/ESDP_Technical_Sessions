class parent:
    def propertice(self):
        print("In the parent class ...")
class chiled(parent):
    def pro(self):
        print("In the child ... ")
class multilevle(chiled):
    def pro_multilevel(self):
        print("In the multilevel..")
object=multilevle()
object.pro_multilevel()
object.propertice()
object.pro()


