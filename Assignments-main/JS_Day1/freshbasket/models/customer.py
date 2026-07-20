from models.person import Person


class Customer(Person):
    """
    Customer inherits Person.
    Demonstrates Encapsulation using private wallet.
    """

    def __init__(self, customer_id, name, age, phone, email, wallet=0):
        super().__init__(customer_id, name, age, phone)

        self.customer_id = customer_id
        self.email = email
        self.__wallet = wallet

    @property
    def wallet(self):
        """Read-only property"""
        return self.__wallet

    def add_money(self, amount):
        if amount > 0:
            self.__wallet += amount

    def purchase(self, amount):
        if amount <= self.__wallet:
            self.__wallet -= amount
            return True
        return False

    def __str__(self):
        return (
            f"Customer ID : {self.customer_id}\n"
            f"Name        : {self.name}\n"
            f"Age         : {self.age}\n"
            f"Phone       : {self.phone}\n"
            f"Email       : {self.email}\n"
            f"Wallet      : ₹{self.wallet}"
        )