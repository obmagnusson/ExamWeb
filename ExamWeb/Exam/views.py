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

@login_required()
def home(request):
    exam = Exam.objects.all()
    model = { "exams" : exam, "u": request.user.username }
    return render_to_response("index.html",model, context_instance=RequestContext(request))

@login_required()
def exam_details(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    #question = Question.objects.filter(exam=exam_id)
    question = Question.objects.filter(exam_id=exam.id)
    #choice = Question.objects.filter(exam_id=exam.id)
    obj = { "exam" : exam , "question" : question}# , "choice" : choice}

    return render_to_response("exam.html" , obj)

def login(request):
    obj = {"next": "/index.html"}
    return render_to_response("login.html", obj)

def logout(request):
    logout(request)
    return render("logout.html")