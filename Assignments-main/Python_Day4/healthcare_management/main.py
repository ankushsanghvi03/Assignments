from models.appointment import Appointment
from models.doctor import Doctor
from models.patient import Patient
from services.healthcare_system import HealthcareSystem
from utils.logger import log_event


# Initialize a simple datastore and the system
system = HealthcareSystem({})

# Create a patient, doctor, and appointment
patient = Patient(1, "John Doe", 30, "Flu")
doctor = Doctor(1, "Dr. Smith", 45, "Cardiology")
appointment = Appointment(1, 1, 1, "2026-07-20", "10:00", "Scheduled")

# Add them to the system
system.patient_service.add_patient(patient)
system.doctor_service.add_doctor(doctor)
system.appointment_service.add_appointment(appointment)

# Display information
log_event("Patient added", system.patient_service.get_patient(1))
log_event("Doctor added", system.doctor_service.get_doctor(1))
log_event("Appointment added", system.appointment_service.get_appointment(1))
