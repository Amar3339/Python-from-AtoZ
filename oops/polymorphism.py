class Car():
    def fuel(self):
        return "petrol"
    
class ev():
    def fuel(self):
        return "electric"
    
    
mycar=Car()
elec=ev()
print(elec.fuel())
print(mycar.fuel())
         