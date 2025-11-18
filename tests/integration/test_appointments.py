from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from appointments.models import Appointment, Dentist, Patient

class AppointmentIntegrationTests(APITestCase):

    def setUp(self):
        self.dentist = Dentist.objects.create(name="Dr. Smith", license_number="12345")
        self.patient = Patient.objects.create(name="John Doe", email="john@example.com")
        self.appointment_data = {
            "dentist": self.dentist.id,
            "patient": self.patient.id,
            "date": "2023-10-01T10:00:00Z",
            "notes": "First appointment"
        }

    def test_create_appointment(self):
        response = self.client.post(reverse('appointment-list'), self.appointment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(Appointment.objects.get().notes, "First appointment")

    def test_get_appointment(self):
        appointment = Appointment.objects.create(**self.appointment_data)
        response = self.client.get(reverse('appointment-detail', args=[appointment.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['notes'], appointment.notes)

    def test_update_appointment(self):
        appointment = Appointment.objects.create(**self.appointment_data)
        updated_data = {"notes": "Updated appointment notes"}
        response = self.client.patch(reverse('appointment-detail', args=[appointment.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        appointment.refresh_from_db()
        self.assertEqual(appointment.notes, "Updated appointment notes")

    def test_delete_appointment(self):
        appointment = Appointment.objects.create(**self.appointment_data)
        response = self.client.delete(reverse('appointment-detail', args=[appointment.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Appointment.objects.count(), 0)