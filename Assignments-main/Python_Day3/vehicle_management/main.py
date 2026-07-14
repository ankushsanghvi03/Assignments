from car import Car
from ev import EV
from polymorphism import Overloadingdemo

car1 = Car("Toyota", "Camry", 2020)
ev1 = EV("Tesla", "Model S", 2021, 100)

car2 = Car("Honda", "Civic", 2019)
ev2 = EV("Nissan", "Leaf", 2020, 40)

car3 = Car("Ford", "Mustang", 2021)
ev3 = EV("Chevrolet", "Bolt", 2021, 60)

car1.set_owner("Ankush")
print(car1.get_owner())  # Output: Ankush

ev1.show_info()
ev1.start_engine()
print(f"Battery Capacity: {ev1.battery_capacity} kWh")

car2.set_owner("Mayur")
print(car2.get_owner())  # Output: Mayur

ev2.show_info()
ev2.start_engine()
print(f"Battery Capacity: {ev2.battery_capacity} kWh")

car3.set_owner("Ayush")
print(car3.get_owner())  # Output: Ayush

ev3.show_info()
ev3.start_engine()
print(f"Battery Capacity: {ev3.battery_capacity} kWh")

cars = [car1, car2, car3]

for car in cars:
    car.show_info()
    car.start_engine()
    print("Owner:", car.get_owner())
    print()