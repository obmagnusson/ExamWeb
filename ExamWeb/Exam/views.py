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

@login_required()
def home(request):
    print "home"
    #exam = ExamResult.objects.filter(student=request.user.id)
    exam = Exam.objects.filter(date_deadline__gt=datetime.utcnow()).order_by('date_deadline')
    model = { "exams" : exam, "u": request.user.username }
    return render_to_response("index.html",model, context_instance=RequestContext(request))

@login_required()
def exam_details(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    question = Question.objects.filter(exam_id=exam.id)
    obj = { "exam" : exam , "question" : question,"u": request.user.username, }

    return render_to_response("exam.html" , obj,context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
def create_exam(request):
    print "create sdaelkmfaldkjf"
    return render_to_response("createExam.html")

@login_required()
def post_exam(request):
    if request.method == 'GET':
        return render_to_response("/")
    else:
        txt = request.POST["createExam"]
        deadline = request.POST["date"]
        e = Exam()
        e.title = txt
        e.date_published = datetime.utcnow()
        e.date_deadline = deadline
        print "Print", request.user
        e.author = request.user
        e.save()
    return  HttpResponseRedirect("/")

@login_required()
def return_exam(request, student_id, exam_id):
    if request.method == 'GET':
        print "skilaget"
        return render_to_response("/")

    else:
        exam = Exam.objects.get(pk=exam_id)
        student = User.objects.get(pk=student_id)
        score = 0.0
        for x in exam.question_set.all():
            print "exid", x.pk
            id = request.POST[str(x.pk)]
            #print "id :", id
            choicevalue = Choice.objects.get(pk=id)
            if choicevalue.isCorrect:
                score +=1

        print "hve oft if setnig:",score
        grade = (score/exam.question_set.count())*10

        #calculate score
        print "Student : ", student
        print "Grade : ", grade
        e = ExamResult()
        e.exam_id = exam_id
        e.student_id = student_id
        e.result = grade
        e.save()
    return  HttpResponseRedirect("/")

def post_questions(request, exam_id):
    if request.method == 'GET':
        print "skilaget"
        return render_to_response("/")

    else:
        q = Question()#Exam.objects.get(exam_id=exam_id)

#        questiontxt = request.POST[]
#        q.exam_id = exam_id
#        q.title = questiontxt
#        c = Choice()



    return HttpResponseRedirect("/")


@login_required()
def exam_results(request, student_id):
    results = ExamResult.objects.filter(student_id=student_id)
    obj = { "results" : results}
    return render_to_response("examResults.html",obj)

@login_required()
def edit_exam(request , exam_id):
    exam = Exam.objects.get(id=exam_id)
    obj ={ "exam" : exam}
    return render_to_response("editExam.html",obj)


def login(request):
    obj = {"next": "/index.html"}
    return render_to_response("login.html", obj)

def logout(request):
    logout(request)
    return render("logout.html")
