import io
from subprocess import IDLE_PRIORITY_CLASS
from urllib import request, response
from django.shortcuts import render
from .models import Employee
import json
from .serializers import EmployeeSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from mainApp import serializers

# Create your views here.
def Home(request):
    return render(request,"index.html")

class EmployeeAPI(APIView):
    # def get(self,request,id=None):
    #         wid = request.query_params.get('id')
    #         wname = request.query_params.get('name')
    #         wemail=request.query_params.get('email')
    #         wdesignation=request.query_params.get('designation')
    #         wsalary=request.query_params.get('salary')
    #         wcity=request.query_params.get('city')
    #         wstate=request.query_params.get('state')
            
    #         if id:
    #             item = Employee.objects.get(empId=id)
    #             serializer = EmployeeSerializer(item)
    #             return Response(serializer.data, status=201)
    #         if wid:
    #             item = Employee.objects.get(empId=wid)
    #             serializer = EmployeeSerializer(item)
    #             return Response(serializer.data, status=201)
    #         if wname:
    #             item = Employee.objects.filter(name=wname)
    #             serializer = EmployeeSerializer(item,many=True)
    #             return Response(serializer.data, status=201)
    #         if wemail:
    #             item = Employee.objects.get(email=wemail)
    #             serializer = EmployeeSerializer(item)
    #             return Response(serializer.data, status=201)
    #         elif wdesignation:
    #             item=Employee.objects.get(designation=wdesignation)
    #             serializer=EmployeeSerializer(item)
    #             return Response(serializer.data,status=201)
    #         elif wsalary:
    #             item=Employee.objects.get(salary=wsalary)
    #             serializer=EmployeeSerializer(item)
    #             return Response(serializer.data,status=201)
    #         elif wcity:
    #             item=Employee.objects.get(city=wcity)
    #             serializer=EmployeeSerializer(item)
    #             return Response(serializer.data,status=201)
    #         if wstate:
    #             item=Employee.objects.filter(state=wstate)
    #             serializer=EmployeeSerializer(item,many=True)
    #             return Response(serializer.data,status=201)
    #         else:   
    #             items = Employee.objects.all()
    #             serializer = EmployeeSerializer(items, many=True)
    #             return Response(serializer.data, status=201)

    def get(self,request):
        try:
            jdata = request.body
            stream = io.BytesIO(jdata)
            pdata = JSONParser().parse(stream)
            wemail = pdata.get("email",None)
            if wemail is not None:
                item = Employee.objects.get(email=wemail)
                serializer = EmployeeSerializer(item)
                print(serializer.data)
                return Response(serializer.data, status=201)
        except:
            items = Employee.objects.all()
            serializer = EmployeeSerializer(items, many=True)
            return Response(serializer.data, status=201)

    def post(self,request):
        jdata = request.body  
        stream = io.BytesIO(jdata)
        pdata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pdata)
        if (serializer.is_valid()):
            serializer.save()
            res = {"msg":"Record Inserted"}
        else:
            res = {"msg":"Record Not Valid"}
        jsondata = JSONRenderer().render(res)
        return HttpResponse(jsondata,content_type="application/json")

    def put(self,request,id=None):
        jdata = request.body    
        stream = io.BytesIO(jdata)
        pdata = JSONParser().parse(stream)
        aemail = pdata.get("email", None)
        if (aemail is not None):
            emp = Employee.objects.get(email=aemail)
            serializer = EmployeeSerializer(emp, data=pdata, partial=True)
            if (serializer.is_valid()):
                serializer.save()
                res = {"msg":"Record updated"}
            else:
                res = {"msg":"Record is invalid"}
        else:
            res={"msg":"No record found to update"}

        jsonData = JSONRenderer().render(res)
        return HttpResponse(jsonData,content_type="application/json")
        
            
    def delete(self,request,id=None):
        jdata = request.body    
        stream = io.BytesIO(jdata)
        pdata = JSONParser().parse(stream)
        aemail = pdata.get("email", None)
        if (aemail is not None):
            emp = Employee.objects.get(email=aemail)
            emp.delete()
            res = {"msg":"Record deleted"}
        else:
            res={"msg":"No record found to delete"}

        jsonData = JSONRenderer().render(res)
        return HttpResponse(jsonData,content_type="application/json")
        
            
