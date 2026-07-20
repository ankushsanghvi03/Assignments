from data.datastore import DATASTORE
from models.account import Account
from utils.validator import (
    is_eligible,
    has_active_membership
)


class AccountService:

    account_counter = 1

    @staticmethod
    def create_account(customer_id, membership_id, months):

        customer = DATASTORE["customers"].get(customer_id)
        membership = DATASTORE["memberships"].get(membership_id)

        if customer is None:
            print("Customer not found.")
            return

        if membership is None:
            print("Membership not found.")
            return

        if not is_eligible(customer):
            print("Customer is below 18 years.")
            return

        if has_active_membership(customer_id):
            print("Customer already has an active membership.")
            return

        amount = membership.calculate_fee(months)

        if not customer.purchase(amount):
            print("Insufficient wallet balance.")
            return

        account = Account(
            f"ACC-{AccountService.account_counter:03d}",
            customer,
            membership,
            months,
            amount,
            "ACTIVE"
        )

        AccountService.account_counter += 1

        DATASTORE["accounts"][account.account_id] = account

        print("Membership account created successfully.")

    @staticmethod
    def renew_membership(account_id, months):

        account = DATASTORE["accounts"].get(account_id)

        if account is None:
            print("Account not found.")
            return

        amount = account.membership.calculate_fee(months)

        if not account.customer.purchase(amount):
            print("Insufficient wallet.")
            return

        account.months += months
        account.amount_paid += amount
        account.status = "ACTIVE"

        setattr(account, "renewal_offer", "5% Cashback")

        print("Membership renewed.")
        print("Offer:", getattr(account, "renewal_offer"))

    @staticmethod
    def expire_membership(account_id):

        account = DATASTORE["accounts"].get(account_id)

        if account:
            account.status = "EXPIRED"
            print("Membership expired.")
        else:
            print("Account not found.")

    @staticmethod
    def delete_membership(account_id):

        if account_id in DATASTORE["accounts"]:
            del DATASTORE["accounts"][account_id]
            print("Membership deleted.")
        else:
            print("Account not found.")

    @staticmethod
    def view_accounts():

        if not DATASTORE["accounts"]:
            print("No membership accounts.")
            return

        for account in DATASTORE["accounts"].values():
            print(account)
            print("-" * 40)