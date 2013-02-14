from __future__ import unicode_literals
from Exam.models import*
#coding: utf8
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import  login_required
from django.shortcuts import *
from django.views.decorators.csrf import csrf_protect


def home(request):
    exam = Exam.objects.all()
    model = { "exams" : exam, "u": request.user.username }
    return render_to_response("index.html",model)

def exam_details(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    #question = Question.get(pk=exam_id)
    obj = { "exam" : exam }

    return render_to_response("exam.html" , obj)
