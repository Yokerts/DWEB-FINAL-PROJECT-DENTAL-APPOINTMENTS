from django.test import TestCase
from .models import Paciente, Odontologo, Cita

class CitaModelTest(TestCase):

    def setUp(self):
        self.paciente = Paciente.objects.create(nombre="Juan Pérez", email="juan@example.com")
        self.odontologo = Odontologo.objects.create(nombre="Dr. Smith", especialidad="Odontología General")
        self.cita = Cita.objects.create(paciente=self.paciente, odontologo=self.odontologo, fecha_hora="2023-10-01 10:00:00")

    def test_cita_creada_correctamente(self):
        self.assertEqual(self.cita.paciente.nombre, "Juan Pérez")
        self.assertEqual(self.cita.odontologo.nombre, "Dr. Smith")
        self.assertEqual(str(self.cita.fecha_hora), "2023-10-01 10:00:00")

    def test_str_metodo_cita(self):
        self.assertEqual(str(self.cita), f"Cita de {self.paciente.nombre} con {self.odontologo.nombre} en {self.cita.fecha_hora}")

class PacienteModelTest(TestCase):

    def setUp(self):
        self.paciente = Paciente.objects.create(nombre="Ana Gómez", email="ana@example.com")

    def test_str_metodo_paciente(self):
        self.assertEqual(str(self.paciente), "Ana Gómez")

class OdontologoModelTest(TestCase):

    def setUp(self):
        self.odontologo = Odontologo.objects.create(nombre="Dr. López", especialidad="Ortodoncia")

    def test_str_metodo_odontologo(self):
        self.assertEqual(str(self.odontologo), "Dr. López")