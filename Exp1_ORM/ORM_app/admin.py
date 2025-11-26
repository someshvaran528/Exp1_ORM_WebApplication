from django.contrib import admin

# Register your models here.
from .models import Student, StudentAdmin
# Register your models here.
admin.site.register(Student, StudentAdmin)