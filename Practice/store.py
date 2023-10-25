class perstore:
    def __init__(self,pet,name,age,price):
        self.pet=pet
        self.name=name
        self.age=age
        self.price=price
        self.details=[]
    def addnewpet(self):
        self.details.append(self.pet,self.name,self.age,self.price)
        print("details added successfully....")
    def searchpet(self):
        n=input("enter the pet you are searching for...")
        for i in self.details:
            if n == i:
                print(self.details[i])
            else:
                print("search not available....")
    def sellpet(self):
        n=input("enter the pet you are searching for...")
        for i in self.details:
            if n == i:
                print(self.details[i][self.price])
                choice=input("do you wish to buy this pet...yes/No")
                if choice == "yes":
                    print("pet sold successfully 😇...for"+self.details[i][self.price])
                else:
                    print("😔")
    def listpet(self):
        print(self.details)

    