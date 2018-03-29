from django.db import models
from apps.login.models import User
from random import choice
import csv, random
import json
from django.http import HttpResponse

class Quiz_Manager(models.Manager):
	def make_chart(self, look_At):
		chart_data = {
			'labels': ["Correct", "Incorrect"],
			'datasets': [{
				'label': "All Data",
				'backgroundColor': ['rgb(132,255,99)','rgb(255, 99, 132)'],
				'borderColor': 'rgb(0, 0, 0)',
				'data': [ len(Quiz.objects.filter(score=1, user = User.objects.get(id=look_At) ) ), len( Quiz.objects.filter(score=0, user = User.objects.get(id=look_At) ) ) ],
			}]
		},
		return HttpResponse(json.dumps(chart_data), content_type="application/json")
	def make_quiz(self, id, dont_repeat):
		all_crap = {}
		quiz = {}
		f_list = dont_repeat
		answer_list = []
		people_list = []
		people_dict = {'people' : People.objects.filter(category = Category.objects.get(id = id))}
		for person in people_dict['people']:
			people_list.append({'athlete': person})
		random.shuffle(people_list)
		#refreshing the page repeatedly will bug this code out...
		for i in range(0,len(people_list)):
			if people_list[i]['athlete'].name not in f_list:
				answer = people_list.pop(i)
				break
		f_list.append(answer['athlete'].name)
		trivia = answer['athlete'].abstract
		answer_list.append({'answer': answer,'value': 1})
		for k in range(0,3):
			answer = people_list.pop()
			answer_list.append({'answer': answer,'value': 0,})
		random.shuffle(answer_list)
		quiz['category'] = Category.objects.get(id=id)
		quiz['trivia'] = trivia
		quiz['answer_list'] = answer_list
		all_crap = {
			'quiz': quiz,
			'dont_repeat': f_list
		}
		return all_crap #and magic

class Category (models.Model):
	activity_type = models.CharField(max_length=255)
	# objects = Catagory_Manager()

class Quiz(models.Model):
	score = models.IntegerField()
	user = models.ForeignKey(
		User, 
		on_delete=models.CASCADE, 
		related_name = "testie"
	)
	
	category = models.ForeignKey(
		Category, 
		on_delete=models.CASCADE, 
		related_name  = "quiz_type"
	)
	objects = Quiz_Manager()

class People(models.Model):
	name = models.CharField(max_length=255)
	abstract = models.TextField(default = "")
	category = models.ForeignKey(
		Category, 
		on_delete=models.CASCADE, 
		related_name  = "category"
	)

	def __repr__(self):
		return f'<Quiz object: {self.name}'






#