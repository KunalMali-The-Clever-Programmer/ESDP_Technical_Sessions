# join its used to excute any other threa before currnt thread is  ready for excution that time its used t1.join() 
#3.creating a thread without extending Thread class
from threading import *

class Mythread:
    def run(self):
        for i in range(1,11):
            print("Child thread.")
m=Mythread()
t=Thread(target=m.run)
t.setDaemon(True)
t.start()
t.join()

for i in range(1,11):
    print("Main thread ")