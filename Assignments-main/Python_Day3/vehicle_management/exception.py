class VehicleError(Exception):
    """Base class for vehicle-related exceptions."""
    pass    

class OwnerAlreadyExsistsError(VehicleError):
    """Raised when trying to add an owner for a vehicle that already has one."""
    def __init__(self, owner_name):
        message = f"Owner '{owner_name}' already exists for this vehicle."
        super().__init__(message)

class InvalidBatteryCapacityError(VehicleError):
    """Raised when an invalid battery capacity is provided for an electric vehicle."""
    def __init__(self, capacity):
        message = f"Invalid battery capacity: {capacity}. Must be a positive number."
        super().__init__("Invalid battery capacity. Must be a positive number.")