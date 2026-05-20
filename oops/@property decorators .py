# use a property decoratirs i car class to make model attreibute read only
class Car:
    def __init__(self, model):
        self.model=model
    
    @property
    def model(self):
         return self.model  
     
car=Car("tata")
print(car.model)      