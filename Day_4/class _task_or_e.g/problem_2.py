class bill:
   rate_30=1.50
   rate_200=3.00
   rate_300=4.25
   ch=0
   
   def __init__(self,p_name,unit):
      
       self.p_name=p_name
       self.unit=unit
   def display(self):
    #    print( f"\t {self.p_name}" )
       if(self.unit<=30):
           ch=self.unit*1.50
           print(f"\t {self.p_name}",f"\t{self.unit}","\t", ch)
       elif(self.unit<=200):
           ch1=30*1.50
           self.unit=self.unit-30
           ch=ch1+self.unit*3.00
           if(ch>=500):
               ch=ch+ch*0.15
           print(f"\t {self.p_name}",f"\t{self.unit}","\t", ch)
       elif(self.unit<=300):
           ch1=30*1.50
           ch=ch1+200*3.00
           self.unit=self.unit-230
           ch=ch+self.unit * 4.00
           if(ch>=500):
               ch=ch+ch*0.15
           print(f"\t {self.p_name}",f"\t{self.unit}","\t", ch)
       else:
           ch1=30*1.50+200*3+70*4.25
           self.unit=self.unit-300
           ch=ch+self.unit * 5.25
           if(ch>=500):
               ch=ch+ch*0.15
           print(f"\t {self.p_name}",f"\t{self.unit}","\t", ch)


list=[]
for i in range(0,1):
    p_name=input("Enter the name :  ")
    unit=int(input("Enter the units : "))
    list1=bill(p_name,unit)
    list.append(list1)
print("\t Name ","\t Units","\t Charges")
for list1 in list:
    list1.display()
       