from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display= [fields.name for fields in Student._meta.get_fields()]