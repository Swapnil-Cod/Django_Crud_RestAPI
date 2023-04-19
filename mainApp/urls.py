from django.urls import URLPattern,path
from .views import EmployeeAPI

urlpatterns=[
    path('employeeapi/',EmployeeAPI.as_view()),
]
