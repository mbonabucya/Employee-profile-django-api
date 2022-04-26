from django.db import models


class Department(models.Model):

    department_Id = models.AutoField(primary_key=True)
    department_Name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_Name

class Employee(models.Model):

    employee_Id = models.AutoField(primary_key=True)
    employee_Name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Join_date= models.DateField()
    profile_Name = models.CharField(max_length = 100)
    def __str__(self):
        return self.employee_Name

