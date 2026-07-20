class Person:
    """
    Base class for all customers.
    """

    def __init__(self, person_id, name, age, phone):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return (
            f"ID : {self.person_id}\n"
            f"Name : {self.name}\n"
            f"Age : {self.age}\n"
            f"Phone : {self.phone}"
        )