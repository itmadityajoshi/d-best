from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentInfoForm
# Create your views here.


def list_student(request):
    student = Student.objects.all() 
    return render(request, 'crud/list_student.html',{"student":student})


def update_student(request,id):
    if request.method == "POST":
     student=Student.objects.get(pk=id)
     fm=StudentInfoForm(request.POST, instance=student)
     if fm.is_valid():
        fm.save()
        return redirect("/")
    else: 
        student=Student.objects.get(pk=id) 
        fm = StudentInfoForm(instance=student)

    return render(request, "crud/update_student.html",{"form":fm })


def delete(request,id):
   stude
