from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exam(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    date_published = models.DateField()
    date_deadline = models.DateField()

class Question(models.Model):
    exam = models.ForeignKey(Exam)
    title = models.CharField(max_length=265)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=256)
    isCorrect = models.BooleanField()

class ExamResult(models.Model):
    result = models.PositiveIntegerField()
    exam = models.ForeignKey(Exam)
    student = models.ForeignKey(User)
