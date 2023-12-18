from django.shortcuts import render
# Create your views here.
from .serializers import CompanySerializer,EmployeesSerializer
from .models import Company,Employees
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
class Companyviewsets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['GET'])
    def employees(self,request,pk=None):
        
        company = Company.objects.get(pk=pk)
        employees = Employees.objects.filter(company=company)
        employees_serializers = EmployeesSerializer(employees,many = True, context = {'request':request})
        
        return Response(employees_serializers.data)


class Employeesviewsets(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

