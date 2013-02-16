from __future__ import unicode_literals
from datetime import datetime
from Exam.models import*
#coding: utf8
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import  login_required, user_passes_test
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
    question = Question.objects.filter(exam_id=exam.id)
    obj = { "exam" : exam , "question" : question}

    return render_to_response("exam.html" , obj)

@user_passes_test(lambda u: u.is_superuser)
def create_exam(request):
    print "create sdaelkmfaldkjf"
    return render_to_response("createExam.html")

def post_exam(request):
    if request.method == 'GET':
        print "jsjejerkj"
        return render_to_response("/")

    else:
        txt = request.POST["createExam"]
        e = Exam()
        e.title = txt
        e.date_published = "2010-12-12"
       # print datetime.now
        print "Heejelkjler"

        e.save()
    return  HttpResponseRedirect("/")


def login(request):
    obj = {"next": "/index.html"}
    return render_to_response("login.html", obj)

def logout(request):
    logout(request)
    return render("logout.html")
