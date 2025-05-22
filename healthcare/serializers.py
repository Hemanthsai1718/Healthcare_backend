from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'gender', 'phone', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']

    def validate_gender(self, value):
        valid_genders = ['M', 'F', 'O']
        if value not in valid_genders:
            raise serializers.ValidationError("Invalid gender. Choose 'M', 'F', or 'O'.")
        return value

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'phone', 'created_at']
        read_only_fields = ['created_at']

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'created_at']
        read_only_fields = ['created_at']

    def validate(self, data):
        if PatientDoctorMapping.objects.filter(patient=data['patient'], doctor=data['doctor']).exists():
            raise serializers.ValidationError("This patient-doctor mapping already exists.")
        return data