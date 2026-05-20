# add a class variable car that keeps track number of total cars

class Car:
          total=0
          
          def __init__(self, brand, model):
              self.brand=brand
              self.model=model
              Car.total+=1
              
class Electric_car(Car):
    def __init__(self,brand, model,type):
        super().__init__(brand,model)
        self.type=type

ev=Electric_car("tesle","s","electric")

                      
          
              
            
              
             
my_car=Car("tata","safari")              
car2=Car("toyota","fortuner")
car3=Car("mahindra","thar")
print(my_car.model)
print(Car.total)
print(ev.model)
print(ev.brand)