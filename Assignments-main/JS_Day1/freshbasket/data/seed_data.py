from data.datastore import DATASTORE

from models.customer import Customer

from models.membership import (
    SilverMembership,
    GoldMembership,
    PremiumMembership
)


def load_seed_data():
    """
    Loads sample memberships and customers
    into the datastore.
    """

    # -------------------------
    # Membership Plans
    # -------------------------

    silver = SilverMembership()
    gold = GoldMembership()
    premium = PremiumMembership()

    DATASTORE["memberships"][silver.membership_id] = silver
    DATASTORE["memberships"][gold.membership_id] = gold
    DATASTORE["memberships"][premium.membership_id] = premium

    # -------------------------
    # Customers
    # -------------------------

    customer1 = Customer(
        "CUS001",
        "Anita",
        24,
        "9876543210",
        "anita@gmail.com",
        3000
    )

    customer2 = Customer(
        "CUS002",
        "Rahul",
        32,
        "9876501234",
        "rahul@gmail.com",
        5000
    )

    customer3 = Customer(
        "CUS003",
        "Kavin",
        16,
        "9876512345",
        "kavin@gmail.com",
        700
    )

    DATASTORE["customers"][customer1.customer_id] = customer1
    DATASTORE["customers"][customer2.customer_id] = customer2
    DATASTORE["customers"][customer3.customer_id] = customer3

    print("Sample data loaded successfully.")