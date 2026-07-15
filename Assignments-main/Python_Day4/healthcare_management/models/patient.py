from models.person import Person

class Patient(Person):
    def __init__(self, id, name, age, ailment):
        super().__init__(id, name, age) #reusable code from Person class
        self.ailment = ailment

    def display_info(self):
        details = super().display_info() #reusable code from Person class
        details.update({"Ailment": self.ailment})
        return details
    