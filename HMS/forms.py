from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'patient_name', 'email', 'phone', 'reason']
        

class HealthMetricsForm(forms.Form):
    blood_pressure = forms.CharField(label='Blood Pressure', max_length=100)
    heart_rate = forms.CharField(label='Heart Rate', max_length=100)
    sugar_levels = forms.CharField(label='Sugar Levels', max_length=100)
