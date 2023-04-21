from django.contrib import admin
from .models import Student
from .models import Employee
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id', 'empName', 'salary']