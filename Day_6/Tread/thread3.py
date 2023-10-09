from threading import *
print(current_thread().getName())
current_thread().setName("Kunal")
print(current_thread().getName())