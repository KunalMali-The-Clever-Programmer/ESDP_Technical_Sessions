class local(object) :
    def fun1(self):
        a=100
        print(a)
    def fun2(self):
        b=222
        a=888
        print(b)
        print(a)

t=local()
t.fun1()
t.fun2()