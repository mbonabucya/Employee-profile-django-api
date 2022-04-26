from django.contrib import admin

from EmployeeData.models import *
# Register your models here.

admin.site.site_header = "Employee Profile "

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_Id', 'employee_Name')
 
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_Id', 'department_Name')