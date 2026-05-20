class Car:
    def __init__(self,model,brand):
        self.model=model
        self.brand =brand
        
my_car=(Car("safari","tata"))
print(my_car.brand) 

class Electric_car(Car):
    def __init__(self,model,brand,battery_size):
        super().__init__(model,brand)
        self.battery_size=battery_size
        
my_ev=Electric_car("tesla","s","1200kwh")  
print(my_ev.model)         
print(my_ev.battery_size) 

class Engine:
    def engine_info(self):
        return "this is high power  engine"
    
class Battery:
    def battery_info(self):
        return "this bateeery have high capacity"
    
class Ev(Electric_car,Engine,Battery):
    pass


mynew_ev=Ev("tesla","s","1200kwh",)
print(mynew_ev.engine_info())
print(mynew_ev.brand)
print(mynew_ev.battery_info())
    
            