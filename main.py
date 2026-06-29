#inheritance
class Car:
    def __init__(self,brand,model,fuel, color):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.color = color

    def getColor(self):
        return self.color
    
    def setColor(self,newColor):
        self.color = newColor
        print(self.color)

    def showCar(self):
        print(f"Car - {self.brand} - {self.model}, Fuel Type - {self.fuel}, Color - {self.color}")

class SUV(Car):
    def __init__(self,brand,model,fuel,color,transmission,turbo):
        Car.__init__(self,brand,model,fuel,color)
        self.transmission = transmission
        self.turbo = turbo
    
    def showCar(self):
        print(f"Car - {self.brand} - {self.model}, Fuel Type - {self.fuel}, Color - {self.color}, Transmission - {self.transmission}, Turbo - {self.turbo}")


FordEscape = SUV("Ford", "Escape ST-Line","Gasoline","Red","Automatic",True)

print(FordEscape.color)
print(FordEscape.getColor())
FordEscape.setColor("white")
FordEscape.showCar() #overridden