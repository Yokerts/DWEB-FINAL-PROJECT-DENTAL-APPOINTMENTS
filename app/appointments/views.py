from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Appointment
from django.shortcuts import render

# Vista para la raíz: citas de hoy
class TodayAppointmentsListView(ListView):
    model = Appointment
    template_name = 'appointments/today_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        today = timezone.localdate()
        return Appointment.objects.filter(date=today).order_by('time')


# CRUD completo de citas
class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = '__all__'
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointments:list')


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'


class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = '__all__'
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointments:list')


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointments:list')

def home_view(request):
    today = timezone.now().date()
    todays_appointments = Appointment.objects.filter(date=today)
    return render(request, 'appointments/home.html', {
        'appointments': todays_appointments
    })