class DoctorService:
    def __init__(self, datastore):
        self.datastore = datastore
        if "doctors" not in self.datastore:
            self.datastore["doctors"] = {}

    def add_doctor(self, doctor):
        self.datastore["doctors"][doctor.id] = doctor

    def get_doctor(self, doctor_id):
        doctor = self.datastore["doctors"].get(doctor_id)
        return doctor.display_info() if doctor else None

    def update_doctor(self, doctor_id, specialty):
        if doctor_id in self.datastore["doctors"]:
            self.datastore["doctors"][doctor_id].specialty = specialty

    def delete_doctor(self, doctor_id):
        if doctor_id in self.datastore["doctors"]:
            del self.datastore["doctors"][doctor_id]
