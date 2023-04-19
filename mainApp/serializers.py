from enum import unique
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    # empId = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    designation = serializers.CharField(max_length=50)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    class Meta:
        model=Employee
        fields=('__all__')


    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if("name" in validated_data):
            instance.name=validated_data["name"]
        
        if("email" in validated_data):
            instance.email=validated_data["email"]

        if("designation" in validated_data):
            instance.designation=validated_data["designation"]

        if("salary" in validated_data):
            instance.salary=validated_data["salary"]
 
        if("city" in validated_data):
            instance.city=validated_data["city"]

        if("state" in validated_data):
            instance.state=validated_data["state"]
 
        instance.save()
        return instance
