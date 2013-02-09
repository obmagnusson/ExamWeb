from __future__ import unicode_literals
from Exam.models import*
#coding: utf8
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    exam = Exam.objects.all()
    model = { "exams" : exam }
    return render_to_response("index.html",model)