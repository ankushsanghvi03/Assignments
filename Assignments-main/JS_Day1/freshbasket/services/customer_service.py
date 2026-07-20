from data.datastore import DATASTORE
from models.customer import Customer


class CustomerService:

    @staticmethod
    def add_customer(customer_id, name, age, phone, email, wallet):

        if customer_id in DATASTORE["customers"]:
            print("Customer already exists.")
            return

        customer = Customer(
            customer_id,
            name,
            age,
            phone,
            email,
            wallet
        )

        DATASTORE["customers"][customer_id] = customer
        print("Customer registered successfully.")

    @staticmethod
    def view_customers():

        if not DATASTORE["customers"]:
            print("No customers found.")
            return

        for customer in DATASTORE["customers"].values():
            print(customer)
            print("-" * 40)

    @staticmethod
    def get_customer(customer_id):
        return DATASTORE["customers"].get(customer_id)

    @staticmethod
    def update_customer(customer_id):

        customer = DATASTORE["customers"].get(customer_id)

        if customer is None:
            print("Customer not found.")
            return

        customer.name = input("Enter new name : ")
        customer.age = int(input("Enter new age : "))
        customer.phone = input("Enter new phone : ")
        customer.email = input("Enter new email : ")

        print("Customer updated successfully.")

    @staticmethod
    def delete_customer(customer_id):

        if customer_id in DATASTORE["customers"]:
            del DATASTORE["customers"][customer_id]
            print("Customer deleted successfully.")
        else:
            print("Customer not found.")