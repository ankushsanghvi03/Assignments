from models.person import Person


class Doctor(Person):
    def __init__(self, id, name, age, specialty):
        super().__init__(id, name, age)
        self.specialty = specialty

    def display_info(self):
        details = super().display_info()
        details.update({"Specialty": self.specialty})
        return details
