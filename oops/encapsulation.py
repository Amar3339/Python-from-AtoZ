class Car():
    def __init__(self):
        self.__brand="tata"
        self.model="sfari"
        
    def get(self):
        return self.__brand
    
mycar=Car()
# print(mycar.__brand)
print(mycar.get())
        
        
        
        