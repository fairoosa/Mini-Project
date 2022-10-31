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


class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week_no = models.IntegerField(null = True, blank = True)
    Title = models.TextField(null = True, blank = True)
    video = models.FileField(null = True, blank = True)
    youtubelink = models.CharField(null = True, blank = True,max_length=300)
    content = models.TextField(null = True, blank = True)
    pdf = models.FileField(null = True, blank = True)




class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.TextField(null = True, blank = True)
    answer = models.TextField(null = True, blank = True)
    option1 = models.TextField(null = True, blank = True)
    option2 = models.TextField(null = True, blank = True)
    option3 = models.TextField(null = True, blank = True)
    option4 = models.TextField(null = True, blank = True)

    # quiz = models.CharField(null = True, blank = True)