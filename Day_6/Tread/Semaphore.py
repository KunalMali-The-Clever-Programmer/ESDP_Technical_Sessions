from threading import *
import time
l=Semaphore(2)
def play(name):
    l.acquire()
    for i in range(10):
        print("Batting :",name)
        time.sleep(1)
    l.release()
t1=Thread(target=play,args=("Rohit",))
t2=Thread(target=play,args=("Gill",))
t3=Thread(target=play,args=("Kohli",))
t4=Thread(target=play,args=("K L Rohul",))
t1.start()
t2.start()
t3.start()
t4.start()
    