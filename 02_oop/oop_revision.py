# OOP Revision Process;

class Car:
    def __init__(self, name, model, power, price):
        self.name = name
        self.model = model
        self.power = power
        self.price = price
        
    
    def printInfo(self):
        print(f"Name= {self.name} , Model= {self.model}, Power= {self.power}, Price= {self.power} .")


c = Car("Honda","Civic","1600",9000000)
c.printInfo()



# ----------constructor--------------

# ----------Inheritance----------------

class ElectricCar(Car):
    def __init__(self,name, model, power, price,battery_power, recharge_capacity):
        super().__init__(name, model, power, price)
        self.__battery_power = battery_power
        self.recharge_capacity = recharge_capacity
        
    
    def printInfo(self):
        super().printInfo()
        print(f"Battery Power = {self.__battery_power}, Recharge Capacity= {self.recharge_capacity}")

e = ElectricCar("Tesla", "E900V", "1500", 12300000, "7500","20 hours")
e.printInfo()




# ----------------ENCAPSULATION-----------------------------

#  JUst place __ before a variable and it becomes private

# print(e.__battery_power)  # Generating Error




























