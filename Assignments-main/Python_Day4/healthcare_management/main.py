from models.patient import Patient
from services.healthcare_system import HealthcareSystem

#Initialize a simple datastore and the system
datastore = {}
system = HealthcareSystem(datastore)

#Create a patient
p1 = Patient(1, "John Doe", 30, "Flu")
p2 = Patient(2, "Jane Smith", 25, "Cold")

#Add Patients to the system
system.patient_service.add_patient(p1)
system.patient_service.add_patient(p2)

#Display Patient Information
print(system.patient_service.get_patient(1))
print(system.patient_service.get_patient(2))