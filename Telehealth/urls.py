import statistics
from django.urls import path
from HMS import views
from Telehealth import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appointments/', views.appointments, name='appointments'),
    path('medication/', views.medication, name='medication'),
    path('reports/', views.reports, name='reports'),
    path('reports/', views.reports_view, name='reports'),
    path('health-tracker/', views.health_tracker_view, name='Health Tracker'),
    path('health-tracker/', views.health_tracker_view, name='health_tracker')
]
    


    


    

