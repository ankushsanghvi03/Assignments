from data.datastore import DATASTORE
from models.membership import (
    SilverMembership,
    GoldMembership,
    PremiumMembership
)


class MembershipService:

    @staticmethod
    def add_membership(choice):

        if choice == 1:
            membership = SilverMembership()

        elif choice == 2:
            membership = GoldMembership()

        elif choice == 3:
            membership = PremiumMembership()

        else:
            print("Invalid choice.")
            return

        DATASTORE["memberships"][membership.membership_id] = membership

        print("Membership added successfully.")
        print(membership)

    @staticmethod
    def view_memberships():

        if not DATASTORE["memberships"]:
            print("No memberships available.")
            return

        for membership in DATASTORE["memberships"].values():
            print(membership)

    @staticmethod
    def get_membership(membership_id):
        return DATASTORE["memberships"].get(membership_id)

    @staticmethod
    def delete_membership(membership_id):

        if membership_id in DATASTORE["memberships"]:
            del DATASTORE["memberships"][membership_id]
            print("Membership deleted.")
        else:
            print("Membership not found.")

    @staticmethod
    def apply_seasonal_discount():

        for membership in DATASTORE["memberships"].values():
            setattr(membership, "festival_discount", 10)

            print(
                membership.membership_name,
                "- Festival Discount:",
                getattr(membership, "festival_discount"),
                "%"
            )