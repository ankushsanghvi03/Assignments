class Membership:
    """
    Base Membership class.
    """

    store_name = "FreshBasket"

    id_prefix = "MEM"
    joining_fee = 0
    counter = 1

    def __init__(self, membership_name, monthly_fee, discount_percentage):

        if monthly_fee <= 0:
            raise ValueError("Monthly fee must be greater than zero.")

        self.membership_id = (
            f"{self.id_prefix}-{Membership.counter:03d}"
        )
        Membership.counter += 1

        self.membership_name = membership_name
        self.monthly_fee = monthly_fee
        self.discount_percentage = discount_percentage

    def calculate_fee(self, months):
        return self.joining_fee + (self.monthly_fee * months)

    def __eq__(self, other):
        return self.monthly_fee == other.monthly_fee

    def __lt__(self, other):
        return self.monthly_fee < other.monthly_fee

    def __str__(self):
        return (
            f"{self.membership_id} | "
            f"{self.membership_name} | "
            f"Monthly Fee : ₹{self.monthly_fee} | "
            f"Discount : {self.discount_percentage}%"
        )


class SilverMembership(Membership):

    id_prefix = "SIL"
    joining_fee = 0

    def __init__(self, monthly_fee=200, discount_percentage=5):
        super().__init__("Silver", monthly_fee, discount_percentage)

    def calculate_fee(self, months):
        return self.monthly_fee * months


class GoldMembership(Membership):

    id_prefix = "GLD"
    joining_fee = 200

    GST_RATE = 0.18

    def __init__(self, monthly_fee=500, discount_percentage=10):
        super().__init__("Gold", monthly_fee, discount_percentage)

    def calculate_fee(self, months):
        base = self.monthly_fee * months
        gst = base * GoldMembership.GST_RATE
        return base + gst + self.joining_fee


class PremiumMembership(Membership):

    id_prefix = "PRE"
    joining_fee = 500

    GIFT_CHARGE = 250

    def __init__(self, monthly_fee=800, discount_percentage=15):
        super().__init__("Premium", monthly_fee, discount_percentage)

    def calculate_fee(self, months):
        base = self.monthly_fee * months
        return base + self.GIFT_CHARGE + self.joining_fee