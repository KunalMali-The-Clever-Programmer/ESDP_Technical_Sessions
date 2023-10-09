#Distroying Objects .....

class des1:
    def __init__(self):
        print("Construter is Call")
    def __del__(self):
        print("Desctrecter is Called ...")
obj=des1()
del des1
