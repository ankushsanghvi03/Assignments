class Account:
    """
    Represents a customer's membership account.
    """

    def __init__(
        self,
        account_id,
        customer,
        membership,
        months,
        amount_paid,
        status="ACTIVE"
    ):
        self.account_id = account_id
        self.customer = customer
        self.membership = membership
        self.months = months
        self.amount_paid = amount_paid
        self.status = status

    def __str__(self):
        return (
            f"\nAccount ID : {self.account_id}\n"
            f"Customer   : {self.customer.name}\n"
            f"Membership : {self.membership.membership_name}\n"
            f"Months     : {self.months}\n"
            f"Amount     : ₹{self.amount_paid}\n"
            f"Status     : {self.status}"
        )

    def __del__(self):
        print("[ARCHIVED] Membership Closed")