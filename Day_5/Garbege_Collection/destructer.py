class des:
    def __init__(self):
        print("If COnstructer is called")
    def __del__(self):
        print("If in the destredter")
t=des()
t=None
print("Program is Closed....")