#2.creating a thread by extending Thread class
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(1,11):
            print("Child Thread..")
m=MyThread()
m.start()
for i in range(1,11):
    print("Main thread.")