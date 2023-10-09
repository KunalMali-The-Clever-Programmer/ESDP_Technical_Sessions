class parent:
    def properties_of_parent(self):
        print("Properties of parent class ...")
class child(parent) :
    def Properties_of_chiled(self):
        print("IN the child class..")
        #also accing parent propoertice ....
object_of_chiled=child()
object_of_chiled.properties_of_parent()
object_of_chiled.Properties_of_chiled()