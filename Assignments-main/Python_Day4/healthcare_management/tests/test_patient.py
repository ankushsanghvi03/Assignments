from models.patient import Patient
from services.healthcare_system import HealthcareSystem


def test_patient_service_crud_flow():
    datastore = {}
    system = HealthcareSystem(datastore)

    patient = Patient(1, "John Doe", 30, "Flu")
    system.patient_service.add_patient(patient)

    stored = system.patient_service.get_patient(1)
    assert stored["Name"] == "John Doe"
    assert stored["Ailment"] == "Flu"

    system.patient_service.update_patient(1, "Migraine")
    updated = system.patient_service.get_patient(1)
    assert updated["Ailment"] == "Migraine"

    system.patient_service.delete_patient(1)
    assert system.patient_service.get_patient(1) is None
