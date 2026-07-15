from models.appointment import Appointment
from services.healthcare_system import HealthcareSystem


def test_appointment_service_flow():
    datastore = {}
    system = HealthcareSystem(datastore)

    appointment = Appointment(1, 1, 2, "2026-07-20", "10:00", "Scheduled")
    system.appointment_service.add_appointment(appointment)

    stored = system.appointment_service.get_appointment(1)
    assert stored["Patient ID"] == 1
    assert stored["Doctor ID"] == 2
    assert stored["Status"] == "Scheduled"

    system.appointment_service.update_appointment_status(1, "Completed")
    updated = system.appointment_service.get_appointment(1)
    assert updated["Status"] == "Completed"

    system.appointment_service.delete_appointment(1)
    assert system.appointment_service.get_appointment(1) is None
