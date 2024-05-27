from vehicle import Vehicle

class Car(Vehicle): # vehicle (class) is added as an argument to the subclass Car so as to be inherited 
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
# We have inherited Car instances from the Vehicle class thus we don't need to write alot 