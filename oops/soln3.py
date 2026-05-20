class Car:
    def __init__(self, brand ,model):
        self.model=model
        self.__brand=brand
    
    def get_brand(self):
        return self.__brand
        
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "diesel and petrol" 
    
    
    
my_car=Car("tata", "safari")
    
class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
    def fuel_type(self):
        return "eletric charge"    
        
ec=Electric_car("tesla","s","80kwh")
# print(ec.brand)
# print(ec.model)
# print(ec.full_name()) 
print(ec.fuel_type()) 
print(my_car.fuel_type())         
        
        
        
        
        
my_car=Car("tata", "safari")
new_car=("suzuki","alto")
# print(my_car.model)
# print(my_car.brand)        
# print(my_car.full_name())    
    