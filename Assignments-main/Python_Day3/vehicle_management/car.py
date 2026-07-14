from exception import OwnerAlreadyExsistsError

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
            #print(f"Owner is {self.__owner}. Cannot change owner.")
            raise OwnerAlreadyExsistsError(self.__owner)
    
    def get_owner(self):
        return self.__owner