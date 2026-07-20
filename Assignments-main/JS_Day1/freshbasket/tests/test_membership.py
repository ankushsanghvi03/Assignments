import unittest

from models.membership import (
    SilverMembership,
    GoldMembership,
    PremiumMembership
)


class TestMembership(unittest.TestCase):

    def test_fee_calculation(self):

        silver = SilverMembership()
        gold = GoldMembership()
        premium = PremiumMembership()

        self.assertEqual(
            silver.calculate_fee(3),
            600
        )

        self.assertGreater(
            gold.calculate_fee(3),
            1500
        )

        self.assertEqual(
            premium.calculate_fee(3),
            3150
        )

    def test_monthly_fee_validation(self):

        with self.assertRaises(ValueError):
            SilverMembership(monthly_fee=-100)


if __name__ == "__main__":
    unittest.main()