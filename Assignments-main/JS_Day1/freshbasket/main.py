from data.seed_data import load_seed_data
from services.store_system import StoreSystem


def main():
    """
    Entry point of the FreshBasket Grocery Store
    Management System.
    """

    # Load sample customers and memberships
    load_seed_data()

    # Start the application
    system = StoreSystem()
    system.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication terminated by user.")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")