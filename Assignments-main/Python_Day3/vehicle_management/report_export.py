# import csv
# def export_vehicle_data(filename, vehicles):
#     """Export vehicle data to a CSV file."""
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Brand', 'Model', 'Year', 'Owner', 'Battery Capacity'])  # Header row

#         for v in vehicles:
#             #handle owner info safely
#             owner = v.get_owner()
#             if owner:
#                 owner = owner.replace('owner: ', '')
#             else:
#                 owner = "No Owner assigned"
#             battery_capacity = getattr(v, 'battery_capacity', 'N/A')  # Get battery capacity if it exists, else 'N/A'
#             writer.writerow([v.brand, v.model, v.year, owner, battery_capacity])
#     return f"Vehicle data exported to {filename} successfully."

import csv

def export_vehicle_data(filename, vehicles):
    """Export vehicle data to a CSV file."""

    with open(filename, mode='w', newline='') as file:

        writer = csv.writer(file)

        writer.writerow(
            ['Brand', 'Model', 'Year', 'Owner', 'Battery Capacity']
        )

        for v in vehicles:

            # Handle owner information safely
            owner = v.get_owner()

            if owner:
                owner = owner.replace('owner: ', '')
            else:
                owner = "No Owner Assigned"

            # Get battery capacity if vehicle is EV
            battery_capacity = getattr(
                v,
                'battery_capacity',
                'N/A'
            )

            writer.writerow([
                v.brand,
                v.model,
                v.year,
                owner,
                battery_capacity
            ])

    return f"Vehicle data exported to {filename} successfully."