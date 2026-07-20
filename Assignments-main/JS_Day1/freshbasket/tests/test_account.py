import unittest

from data.datastore import DATASTORE

from models.customer import Customer
from models.membership import SilverMembership

from services.account_service import AccountService


class TestAccount(unittest.TestCase):

    def setUp(self):

        DATASTORE["customers"].clear()
        DATASTORE["memberships"].clear()
        DATASTORE["accounts"].clear()

        customer = Customer(
            "CUS001",
            "Anita",
            24,
            "9876543210",
            "anita@gmail.com",
            5000
        )

        membership = SilverMembership()

        DATASTORE["customers"][customer.customer_id] = customer
        DATASTORE["memberships"][membership.membership_id] = membership

    def test_successful_membership_creation(self):

        membership_id = list(
            DATASTORE["memberships"].keys()
        )[0]

        AccountService.create_account(
            "CUS001",
            membership_id,
            3
        )

        self.assertEqual(
            len(DATASTORE["accounts"]),
            1
        )

    def test_underage_customer_rejection(self):

        underage = Customer(
            "CUS002",
            "Kavin",
            16,
            "9876500000",
            "kavin@gmail.com",
            3000
        )

        DATASTORE["customers"][
            underage.customer_id
        ] = underage

        membership_id = list(
            DATASTORE["memberships"].keys()
        )[0]

        AccountService.create_account(
            "CUS002",
            membership_id,
            2
        )

        self.assertEqual(
            len(DATASTORE["accounts"]),
            0
        )


if __name__ == "__main__":
    unittest.main()