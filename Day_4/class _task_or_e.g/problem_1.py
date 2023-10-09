class Team:
   list=[]
   def __init__(self,country,p_name,match,age,bat_avg,bal_avg):
       self.country=country
       self.p_name=p_name
       self.match=match
       self.age=age
       self.bat_avg=bat_avg
       self.bal_avg=bal_avg
   def display(self):
    #    print("\t country","\t Name ","\t Matchs","\t Age","\tBatting avg ","\t Balling avg")
       print( f"\t {self.country}",f"\t\t {self.p_name}",f"\t {self.match}",f"\t\t {self.age}",f"\t\t {self.bat_avg}",f"\t\t {self.bal_avg}", )
        
list=[]
for i in range(0,1):
    country=input("Enter the country of Player : ")
    p_name=input("Enter the name of player:  ")
    match=int(input("Enter the name of match played in their carear: "))
    age=int(input("Enter the age :  "))
    bat_avg=int(input("Enter the batting avege :  "))
    bal_avg=int(input("Enter the balling avrege :  "))
    list1=Team(country,p_name,match,age,bat_avg,bal_avg)
    list.append(list1)
print("\t country","\t Name ","\t Matchs","\t Age","\tBatting avg ","\t Balling avg")
for list1 in list:
    list1.display()
       