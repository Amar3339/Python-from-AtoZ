# add a static method that returns general description of cars

class Car:

    def __init__(self,brand ,model):
        self.brand=brand
        self.model=model
    @staticmethod #this is decorators in python its stop to acess the value by using instances and give the value byusing class
             
    def car_derscription():#we dont use self becasuse its ask for static mthod to find the description by using only class not instances(object)
                 return "car is source of transportation"
    # self is used for linkage if instances
        
        
    
    
    
my_car=Car("tata","safari")
print(Car.car_derscription())    
    
    
    