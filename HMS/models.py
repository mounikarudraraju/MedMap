from django.db import models

class Appointment(models.Model):
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    patient_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient_name} - {self.doctor} - {self.date}"

class Report(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_dob = models.DateField()
    doctor_name = models.CharField(max_length=255)
    date = models.DateField()
    report_file = models.FileField(upload_to='reports/')  # Assuming reports will be uploaded and stored in a 'reports/' directory

    def __str__(self):
        return f"Report for {self.patient_name} - {self.date}"
