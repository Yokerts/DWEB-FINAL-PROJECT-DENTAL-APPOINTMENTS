from rest_framework import serializers
from .models import Patient, Dentist, Appointment


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    dentist = DentistSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        dentist_data = validated_data.pop('dentist')

        patient = Patient.objects.create(**patient_data)
        dentist = Dentist.objects.create(**dentist_data)

        appointment = Appointment.objects.create(
            patient=patient,
            dentist=dentist,
            **validated_data
        )
        return appointment

    def update(self, instance, validated_data):
        patient_data = validated_data.pop('patient', None)
        dentist_data = validated_data.pop('dentist', None)

        if patient_data:
            for attr, value in patient_data.items():
                setattr(instance.patient, attr, value)
            instance.patient.save()

        if dentist_data:
            for attr, value in dentist_data.items():
                setattr(instance.dentist, attr, value)
            instance.dentist.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
