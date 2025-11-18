from django.contrib import admin
from .models import Patient, Dentist, Appointment

# Admin para Dentist
@admin.register(Dentist)
class DentistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty')  # usa los campos existentes
    search_fields = ('first_name', 'last_name', 'specialty')
    list_filter = ('specialty',)

# Admin para Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')  # usa los campos existentes
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ()

# Admin para Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'dentist', 'date', 'time', 'status')
    search_fields = ('patient__first_name', 'patient__last_name',
                     'dentist__first_name', 'dentist__last_name')
    list_filter = ('status', 'date', 'dentist')
