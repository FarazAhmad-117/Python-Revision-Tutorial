class Car:
    def __init__(self,brand ="Unknown",model='Unknown'):
        self.brand = brand
        self.model = model
        
    def get_info(self):
        print(f"{self.brand} has made {self.model} this week!")


a = Car('Audi','V8')
a.get_info()

b = Car('Merceries','DEPTA 8')
b.get_info()



