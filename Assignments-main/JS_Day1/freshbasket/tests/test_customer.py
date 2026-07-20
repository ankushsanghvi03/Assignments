import unittest

from models.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_customer_creation(self):

        customer = Customer(
            "CUS001",
            "Anita",
            24,
            "9876543210",
            "anita@gmail.com",
            3000
        )

        self.assertEqual(customer.customer_id, "CUS001")
        self.assertEqual(customer.name, "Anita")
        self.assertEqual(customer.wallet, 3000)

    def test_wallet_encapsulation(self):

        customer = Customer(
            "CUS002",
            "Rahul",
            32,
            "9876501234",
            "rahul@gmail.com",
            5000
        )

        customer.add_money(1000)

        self.assertEqual(customer.wallet, 6000)

        result = customer.purchase(2000)

        self.assertTrue(result)
        self.assertEqual(customer.wallet, 4000)


if __name__ == "__main__":
    unittest.main()