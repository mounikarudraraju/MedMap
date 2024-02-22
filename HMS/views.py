from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from .models import Report  
from .forms import HealthMetricsForm

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def medication(request):
    return render(request, 'medication.html') 

def reports(request):
    return render(request, 'reports.html') 

def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Redirect to a success page
    else:
        form = AppointmentForm()
    
    return render(request, 'appointments.html', {'form': form}) 

def reports_view(request):
    reports = Report.objects.all()  # Query all reports, you may need to adjust this query
    return render(request, 'reports.html', {'reports': reports})


def health_tracker_view(request):
    if request.method == 'POST':
        form = HealthMetricsForm(request.POST)
        if form.is_valid():
            # Process the form data
            blood_pressure = form.cleaned_data['blood_pressure']
            heart_rate = form.cleaned_data['heart_rate']
            sugar_levels = form.cleaned_data['sugar_levels']
            # Process and save the data as needed

            # For demonstration purposes, let's assume we save to a database
            # Here you would save the data to your models or perform other actions

            # Redirect after a successful POST
            return redirect('health_tracker')  # Redirect to the same page to refresh the table
    else:
        form = HealthMetricsForm()

    # Fetch previously entered data for demonstration (you would query your database here)
    # For demonstration purposes, I'm creating sample data
    health_data = [
        {'blood_pressure': '120/80', 'heart_rate': '75', 'sugar_levels': '100'},
        {'blood_pressure': '130/85', 'heart_rate': '80', 'sugar_levels': '110'},
        # Add more sample data as needed
    ]

    context = {
        'form': form,
        'health_data': health_data,  # Pass the health data to display in the table
    }
    return render(request, 'health_tracker.html', context)

