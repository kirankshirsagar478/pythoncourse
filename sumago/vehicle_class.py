#Define a class attribute "colour" with a default value white. I.e., 
#Every vehicle should be white.
class Vehicle:
    color = "white"

    def __init__(self):
        
        pass

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

#default color is white
car = Vehicle()
print(car.get_color())  

car.set_color("blue")
print(car.get_color())  

truck = Vehicle()
print(truck.get_color())  

bike= Vehicle()
bike.set_color("Red")
print (bike.get_color())