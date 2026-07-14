class Car:

    def __init__(self, brand, model, year, owner=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.__owner = owner

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

    def show_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
    
    def set_owner(self, owner):
        if not self.__owner:
            self.__owner = owner
        else:
            print(f"Owner is {self.__owner}. Cannot change owner.")
    
    def get_owner(self):
        return self.__owner

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)

car1.set_owner("Ankush")

car2.set_owner("Mayur")

car3.set_owner("Ayush")

cars = [car1, car2, car3]

for car in cars:
    car.show_info()
    car.start_engine()
    print("Owner:", car.get_owner())
    print()