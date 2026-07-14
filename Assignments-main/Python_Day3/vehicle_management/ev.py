from car import Car
class EV(Car):
    def __init__(self, brand, model, year, battery_capacity, owner=None):
        super().__init__(brand, model, year, owner)
        self.battery_capacity = battery_capacity    

    def start_engine(self):
        print(f"{self.brand} {self.model} electric engine started.")

    def charge_battery(self):
        print(f"{self.brand} {self.model} is charging. Battery capacity: {self.battery_capacity} kWh.")
