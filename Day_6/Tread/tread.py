#1.creating a thread without using any class
from threading import *

def show ():
    for i in range (1,11):
        print("Child thread..")

t=Thread(target=show)
t.start()
for i in range(1,11):
    print("Main thread..")
