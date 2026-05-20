class Car:
    def __init__(self, brand ,model):
        self.model=model
        self.brand=brand
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    
class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
ec=Electric_car("tesla","s","80kwh")
print(ec.brand) 
print(ec.model)
print(ec.full_name())           
        
        
        
        
        
my_car=Car("tata", "safari")
new_car=("suzuki","alto")
print(my_car.model)
print(my_car.brand)        
print(my_car.full_name())    
    