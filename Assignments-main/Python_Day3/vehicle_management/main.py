# from car import Car
# from ev import EV
# from polymorphism import Overloadingdemo

# car1 = Car("Toyota", "Camry", 2020)
# ev1 = EV("Tesla", "Model S", 2021, 100)

# car2 = Car("Honda", "Civic", 2019)
# ev2 = EV("Nissan", "Leaf", 2020, 40)

# car3 = Car("Ford", "Mustang", 2021)
# ev3 = EV("Chevrolet", "Bolt", 2021, 60)

# car1.set_owner("Ankush")
# print(car1.get_owner())  # Output: Ankush

# ev1.show_info()
# ev1.start_engine()
# print(f"Battery Capacity: {ev1.battery_capacity} kWh")

# car2.set_owner("Mayur")
# print(car2.get_owner())  # Output: Mayur

# ev2.show_info()
# ev2.start_engine()
# print(f"Battery Capacity: {ev2.battery_capacity} kWh")

# car3.set_owner("Ayush")
# print(car3.get_owner())  # Output: Ayush

# ev3.show_info()
# ev3.start_engine()
# print(f"Battery Capacity: {ev3.battery_capacity} kWh")

# cars = [car1, car2, car3]

# for car in cars:
#     car.show_info()
#     car.start_engine()
#     print("Owner:", car.get_owner())
#     print()

from car import Car
from ev import EV
from report_export import export_vehicle_data   # your CSV file name


# -----------------------------
# Create Vehicles
# -----------------------------

car1 = Car("Toyota", "Camry", 2020)
ev1 = EV("Tesla", "Model S", 2021, 100)

car2 = Car("Honda", "Civic", 2019)
ev2 = EV("Nissan", "Leaf", 2020, 40)

car3 = Car("Ford", "Mustang", 2021)
ev3 = EV("Chevrolet", "Bolt", 2021, 60)


# -----------------------------
# Assign Owners
# -----------------------------

owners = ["Ankush", "Mayur", "Ayush"]

cars = [car1, car2, car3]
evs = [ev1, ev2, ev3]


for car, ev, owner in zip(cars, evs, owners):
    car.set_owner(owner)
    ev.set_owner(owner)


# -----------------------------
# Display Vehicle Information
# -----------------------------

print("=" * 50)
print("        VEHICLE MANAGEMENT SYSTEM")
print("=" * 50)


for index, (car, ev) in enumerate(zip(cars, evs), start=1):

    print(f"\nVehicle #{index}")
    print("-" * 50)

    print("🚗 Car Details")
    car.show_info()
    car.start_engine()
    print("Owner:", car.get_owner())

    print()

    print("⚡ Electric Vehicle Details")
    ev.show_info()
    ev.start_engine()
    ev.charge_battery()
    print("Owner:", ev.get_owner())

    print("-" * 50)


# -----------------------------
# Export Data to CSV
# -----------------------------

all_vehicles = cars + evs

message = export_vehicle_data(
    "vehicles.csv",
    all_vehicles
)

print("\n📁", message)