class PatientService:
    def __init__(self, datastore):
        self.datastore = datastore
        if "patients" not in self.datastore:
            self.datastore["patients"] = {}

    def add_patient(self, patient):
        self.datastore["patients"][patient.id] = patient

    def get_patient(self, patient_id):
        patient = self.datastore["patients"].get(patient_id)
        return patient.display_info() if patient else None

    def update_patient(self, patient_id, ailment):
        if patient_id in self.datastore["patients"]:
            self.datastore["patients"][patient_id].ailment = ailment

    def delete_patient(self, patient_id):
        if patient_id in self.datastore["patients"]:
            del self.datastore["patients"][patient_id]