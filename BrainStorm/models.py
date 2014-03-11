from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from profiles.models import UserProfile
from tinymce.models import HTMLField


class Session(models.Model):
    content = HTMLField()
    #class Media:
      #  js = ('/static/tiny_mce/tiny_mce.js',
     #         '/static/tiny_mce/my_advanced_editor.js')



class Courses(models.Model):
    lector = models.ForeignKey(UserProfile)
    title = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=100)

class StudentsCourses(models.Model):
    student = models.ForeignKey(UserProfile)
    course = models.ForeignKey(Courses)
    subscribe_date = models.DateField()

class Lecturers(models.Model):
    course = models.ForeignKey(Courses)
    title = models.CharField(max_length=50)
    text = models.TextField()

class Videos(models.Model):
    lecture = models.ForeignKey(Lecturers)

class Comments(models.Model):
    course = models.ForeignKey(Courses, null=True)
    text = models.TextField(null=False, max_length=100)
    user_name = models.CharField(max_length=20)

