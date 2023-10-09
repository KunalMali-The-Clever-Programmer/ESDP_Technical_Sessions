class outer:
    def __init__(self):
        print("In the outer class...........")
    class inner:
        def __init__(self):
            print("In the inner class............")
        def fun(self):
            print("IN the inner class agahin ......")

obj=outer()
i=obj.inner()
i.fun()
print('~'*100)
i1=outer().inner()
i1.fun()