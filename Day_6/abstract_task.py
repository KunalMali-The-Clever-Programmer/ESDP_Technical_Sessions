from abc import ABC ,abstractmethod
class product(ABC):
    @abstractmethod
    def get_price(self):
        # self.name=name
        # self.price=price
        pass
    
    @abstractmethod
    def Display_price(self):
        pass

class electronic(product):
    def get_price(self):
        self.name=input("Enter the Name of product: ")
        self.price=int(input("Enter the price of product: "))
        self.brand=input("Enter the Brand of product: ")
        self.warrenty=int(input("Enter the warrenty of product in Years : "))

    def Display_price(self):
        print(" Name of product: ",self.name)
        print(" price of product: ",self.price)
        print(" Brand of product: ",self.brand)
        print("warrenty of product in Years : ",self.warrenty)

class Clothing(product):
    def get_price(self):
        self.name=input("Enter the Name of Clothing: ")
        self.price=int(input("Enter the price of Clothing: "))
        self.size=int(input("Enter the size of Clothing: "))
        self.color=input("Enter the color of Clothing: ")
        self.material=input("Enter the material of Clothing: ")

    def Display_price(self):
        print(" Name of Clothing: ",self.name)
        print(" price of Clothing: ",self.price)
        print(" size of Clothing: ",self.size)
        print("color of Clothing: ",self.color)
        print("material of Clothing: ",self.material)
        
class Books(product):
    def get_price(self):
        self.name=input("Enter the Name of Book: ")
        self.price=int(input("Enter the price of Book: "))
        self.another=input("Enter the another of Book: ")
        self.genre=input("Enter the genre of Book: ")
        

    def Display_price(self):
        print(" Name of Book: ",self.name)
        print(" price of Book: ",self.price)
        print(" another of Book: ",self.another)
        print("genre of Clothing: ",self.genre)

        #FOR TABLE STRUTURE OUTPUT
        # print("Name","\tprice","\tanother","\tgenre")
        # print(f"{self.name}",f"\t{self.price}",f"\t{self.another}",f"\t{self.genre}",)

        #USING RETURN WORD 
        # n=" Name of Book: ",self.name
        # p=" price of Book: ",self.price
        # return n,p


object_of_book_class=Books()
object_of_book_class.get_price()
object_of_book_class.Display_price()

# object_of_electronic_class=electronic()
# object_of_electronic_class.get_price()
# object_of_electronic_class.Display_price()

# object_of_Clothing_class=Clothing()
# object_of_Clothing_class.get_price()
# object_of_Clothing_class.Display_price()