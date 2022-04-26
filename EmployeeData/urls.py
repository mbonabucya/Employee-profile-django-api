

from django.urls import path,include
from .views import *
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register('Departments', views.Departments)
#router.register('posts', views.PostViewSet)
 
urlpatterns = [
    #path('', include(router.urls)),
    path('departments/', Departments.as_view()),
    path('departments/<int:department_Id>/', Department_RUD.as_view()),
    path('employees/', Employees.as_view()),
    path('employees/<int:employee_Id>/', Employee_RUD.as_view())
 
]