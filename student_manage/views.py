from django.shortcuts import render
from .models import Student
# Create your views here.


def list_student(request):
    student = Student.objects.all() 
    return render(request, 'crud/list_student.html',{"student":student})