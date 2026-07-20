from services.customer_service import CustomerService
from services.membership_service import MembershipService
from services.account_service import AccountService


class StoreSystem:

    def run(self):

        while True:

            print("\n========== FreshBasket Store ==========")
            print("1. Register Customer")
            print("2. Add Membership")
            print("3. View Memberships")
            print("4. Create Membership Account")
            print("5. Renew Membership")
            print("6. Expire Membership")
            print("7. View Accounts")
            print("8. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:

                cid = input("Customer ID : ")
                name = input("Name : ")
                age = int(input("Age : "))
                phone = input("Phone : ")
                email = input("Email : ")
                wallet = float(input("Wallet : "))

                CustomerService.add_customer(
                    cid,
                    name,
                    age,
                    phone,
                    email,
                    wallet
                )

            elif choice == 2:

                print("1. Silver")
                print("2. Gold")
                print("3. Premium")

                plan = int(input("Choose Membership : "))
                MembershipService.add_membership(plan)

            elif choice == 3:

                MembershipService.view_memberships()

            elif choice == 4:

                cid = input("Customer ID : ")
                mid = input("Membership ID : ")
                months = int(input("Months : "))

                AccountService.create_account(
                    cid,
                    mid,
                    months
                )

            elif choice == 5:

                aid = input("Account ID : ")
                months = int(input("Renew Months : "))

                AccountService.renew_membership(
                    aid,
                    months
                )

            elif choice == 6:

                aid = input("Account ID : ")
                AccountService.expire_membership(aid)

            elif choice == 7:

                AccountService.view_accounts()

            elif choice == 8:

                print("Thank you for using FreshBasket.")
                break

            else:
                print("Invalid choice.")