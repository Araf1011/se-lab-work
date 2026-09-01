from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer

def studentview(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(data=serializer.data)
    return HttpResponse(json_data)

def studentListview(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    json_data = JSONRenderer().render(data=serializer.data)
    return HttpResponse(json_data)
# Create your views here.
