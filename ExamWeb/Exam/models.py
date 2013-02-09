from django.db import models

# Create your models here.
class Exam(models.Model):
    title = models.CharField(max_length=256)
    date_published = models.DateField()

class Question(models.Model):
    exam = models.ForeignKey(Exam)
    title = models.CharField(max_length=265)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=256)
    isCorrect = models.BooleanField()
