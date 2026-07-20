from data.datastore import DATASTORE


def is_eligible(customer):
    """
    Customer must be above 18 years.
    """
    return customer.age > 18


def has_active_membership(customer_id):
    """
    Returns True if customer already has
    an ACTIVE membership.
    """

    for account in DATASTORE["accounts"].values():

        if (
            account.customer.customer_id == customer_id
            and account.status == "ACTIVE"
        ):
            return True

    return False


def positive_integer(value):
    """
    Validate positive integer.
    """

    try:
        value = int(value)

        if value > 0:
            return value

        raise ValueError

    except ValueError:
        raise ValueError("Enter a positive integer.")