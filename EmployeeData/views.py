from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import mixins, viewsets,generics


class Departments(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                    ):
    serializer_class = department_Serializer
    queryset = Department.objects.all()
 
    def get(self, request):
        return self.list(request)
 
 
 
    def post(self, request):
        return self.create(request)
 
 
 
class Department_RUD(generics.GenericAPIView,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
 
    serializer_class = department_Serializer
    queryset = Department.objects.all()
    
    lookup_field = 'department_Id'
 
 
    def get(self, request, department_Id):
        return self.retrieve(request, department_Id=department_Id)
 
    def put(self, request, department_Id=None):
        return self.update(request, department_Id)
 
    def delete(self, request, department_Id):
        return self.destroy(request, department_Id)





class Employees(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                    ):
    serializer_class = employee_Serializer
    queryset = Employee.objects.all()
 
    def get(self, request):
        return self.list(request)
 
    def post(self, request):
        return self.create(request)
 
 
 
class Employee_RUD(generics.GenericAPIView,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
 
    serializer_class = employee_Serializer
    queryset = Employee.objects.all()
    
    lookup_field = 'employee_Id'
 
 
    def get(self, request,employee_Id ):
        return self.retrieve(request, employee_Id=employee_Id)
 
    def put(self, request, employee_Id=None):
        return self.update(request, employee_Id)
 
    def delete(self, request, employee_Id):
        return self.destroy(request, employee_Id)





