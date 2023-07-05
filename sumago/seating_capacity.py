#create a bus class that inherits from the vehicle class.
#Give the capacity argument of bus. seating_capacity() a
#default valule of 50
# class Vehicle:
#     def __init__(self, max_speed, name, mileage):
#         self.max_speed = max_speed
#         self.name = name
#         self.mileage = mileage


#     def seating_capacity(self,capacity):
#         return f"Seating capacity of {self.name} is {capacity} passengers. "

class Vehicle:
    def __init__(self, max_speed, name, mileage):
        self.max_speed = max_speed
        self.name = name
        self.mileage = mileage

    # def start_engine(self):
    #     print("Engine started.")

    # def stop_engine(self):
    #     print("Engine stopped.")


class Bus(Vehicle):
    def __init__(self, max_speed, name, mileage, capacity=50):
        super().__init__(max_speed, name, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        print(f"The bus has a seating capacity of {self.capacity} passengers.")


# Example usage
my_bus = Bus("ABC Bus Company", "XYZ Bus Model", 2023)
my_bus.seating_capacity()  #seating capacity of 50

another_bus = Bus("DEF Bus Company", "123 Bus Model", 2022, 60)
another_bus.seating_capacity()  #seating capacity of 60.

#task: search info about
#metadata
#what is modules in python and packages in python with examples.