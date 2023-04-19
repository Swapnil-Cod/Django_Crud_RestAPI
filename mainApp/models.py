
from django.db import models

# Create your models here.
class Employee(models.Model):
    empId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=20)
    salary = models.IntegerField(null=True)
    city = models.CharField(max_length=20, default=None, blank=True, null=True)
    state = models.CharField(max_length=20, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.empId)+"   "+ self.name