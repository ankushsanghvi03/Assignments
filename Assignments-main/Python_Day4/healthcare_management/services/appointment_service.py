class AppointmentService:
    def __init__(self, datastore):
        self.datastore = datastore
        if "appointments" not in self.datastore:
            self.datastore["appointments"] = {}

    def add_appointment(self, appointment):
        self.datastore["appointments"][appointment.id] = appointment

    def get_appointment(self, appointment_id):
        appointment = self.datastore["appointments"].get(appointment_id)
        return appointment.display_info() if appointment else None

    def update_appointment_status(self, appointment_id, status):
        if appointment_id in self.datastore["appointments"]:
            self.datastore["appointments"][appointment_id].status = status

    def delete_appointment(self, appointment_id):
        if appointment_id in self.datastore["appointments"]:
            del self.datastore["appointments"][appointment_id]
