class count_obj:
    count=0
    def __init__(self):
        count_obj.count=count_obj.count+1

    @classmethod
    def shownoobj(cls):
        print("The Number of object are creta is : ",cls.count)

t=count_obj()
t1=count_obj()

count_obj.shownoobj()
t2=count_obj()
t3=count_obj()
count_obj.shownoobj()