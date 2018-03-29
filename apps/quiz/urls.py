from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.quiz, name = 'quiz_home'),
    path('<int:id>', views.create_quiz, name = 'create_quiz'),
    path('submit/<int:id>', views.submit_quiz, name = 'submit_quiz'),
    path('end', views.quiz_end, name = 'quiz_end'),
    path('quiz_stats', views.quiz_stats, name = 'quiz_stats'),
    path('make_chart', views.make_chart, name = 'make_chart')
    ]
