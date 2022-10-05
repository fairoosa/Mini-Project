from django.contrib import admin
from admin_management.models import University, Faculty
from Course.models import Course

admin.site.register(University)
admin.site.register(Course)
admin.site.register(Faculty)

