from rest_framework import  serializers
from .models import *
 
 
class department_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = Department
        fields = '__all__'
 
class employee_Serializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employee
        fields = '__all__'