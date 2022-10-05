from django.db import models
from admin_management.models import University, Faculty

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.course_name