class Rcpit:
    def __init__(self):
        print("DEfult Constructer of Rcpit : ")
    class computer_dep:
        def __init__(self):
            print("Computer Department of defult construter : ")
        def Tech(self):
            print("Rcpit and Computer Department tech")

r=Rcpit()
r1=r.computer_dep()
obj=Rcpit().computer_dep()
obj.Tech()
Rcpit().computer_dep().Tech()
