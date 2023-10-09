#3.creating a thread without extending Thread class
from threading import *

class Mythread:
    def run(self):
        for i in range(1,11):
            print("Child thread.")
m=Mythread()
t=Thread(target=m.run)
t.start()

for i in range(1,11):
    print("Main thread ")