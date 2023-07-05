#Write a python program to create a vehicle class with max_speed,
#name and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, name, mileage):
        self.max_speed = max_speed
        self.name = name
        self.mileage = mileage

    

car = Vehicle(200, "Car", 15)
bike = Vehicle(180, "Bike", 40)

print(f"Car Name:{car.name} \tmaximum speed: {car.max_speed} km/h \tmileage: {car.mileage} km/l.")
print(f"Bike Name:{bike.name}\tmaximum speed: {bike.max_speed} km/h \tmileage: {bike.mileage} km/l.")
