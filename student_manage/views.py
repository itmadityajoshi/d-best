from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentInfoForm
from django.db.models import Q
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
    if request.method == "POST":
       student=Student.objects.get(pk=id)
       student.delete()
       return redirect('/')
    

def add_student(requset):
    if requset.method == "POST":
       fm=StudentInfoForm(requset.POST)
       if fm.is_valid():
          fm.save()
          return redirect ('/')
    else:
        fm=StudentInfoForm()
    return render(requset, 'crud/add_student.html', {"form":fm})

def search_student(request):
   if request.method == "POST":
      search = request.POST.get("output")
      student = Student.objects.all()
      if search:
         std = student.filter(
            Q(fname__icontains=search)|
            Q(lname__icontains=search)|
            Q(email__icontains=search)|
            Q(branch__icontains=search)
            )
      return render(request, 'crud/list_student.html', {"student": std})
   else:
      return render(request, 'crud/list_student.html')