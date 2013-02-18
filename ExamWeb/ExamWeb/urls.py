from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ExamWeb.views.home', name='home'),
    # url(r'^ExamWeb/', include('ExamWeb.foo.urls')),
    (r'^assembled/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),

    url(r'^$', 'Exam.views.home'),
    url(r'^createExam$', 'Exam.views.create_exam'),
    url(r'^exams/(\d+)$', 'Exam.views.exam_details'),
    url(r'^createExam/post_exam', 'Exam.views.post_exam'),
    url(r'^editExam/(\d+)$', 'Exam.views.edit_exam'),
    url(r'^exams/(\d+)/return_exam/(\d+)$', 'Exam.views.return_exam'),
    url(r'^examResults/(\d+)$', 'Exam.views.exam_results'),


    (r'^accounts/$','django.contrib.auth.views.login'),
    (r'^accounts/login/$','django.contrib.auth.views.login'),
    (r'^accounts/logout/$','django.contrib.auth.views.logout'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
