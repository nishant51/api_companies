from rest_framework import serializers
from .models import Company, Employees  # Make sure to import your Company and Employees models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees  # Specify the model that the serializer is associated with
        fields = '__all__'
