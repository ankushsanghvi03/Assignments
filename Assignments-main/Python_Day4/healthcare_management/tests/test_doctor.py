from models.doctor import Doctor
from services.healthcare_system import HealthcareSystem


def test_doctor_service_crud_flow():
    datastore = {}
    system = HealthcareSystem(datastore)

    doctor = Doctor(1, "Dr. Smith", 45, "Cardiology")
    system.doctor_service.add_doctor(doctor)

    stored = system.doctor_service.get_doctor(1)
    assert stored["Name"] == "Dr. Smith"
    assert stored["Specialty"] == "Cardiology"

    system.doctor_service.update_doctor(1, "Neurology")
    updated = system.doctor_service.get_doctor(1)
    assert updated["Specialty"] == "Neurology"

    system.doctor_service.delete_doctor(1)
    assert system.doctor_service.get_doctor(1) is None
