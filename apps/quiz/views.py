from django.shortcuts import render, HttpResponse, redirect
from time import sleep
from apps.quiz.models import *
from apps.login.models import *
from operator import itemgetter

def quiz(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context = {
		'categories' : Category.objects.all(),
		'user': User.objects.get(id=request.session['user_id']),
		}
	return render(request, 'quiz/quiz.html', context)

def create_quiz(request, id):
	if 'user_id' not in request.session:
		return redirect('/')
	request.session['cat_id'] = id
	if 'dont_repeat' not in request.session:
		request.session['dont_repeat'] = []
	if len(request.session['dont_repeat']) > 7:
		request.session['dont_repeat'] = []
	trivia = Quiz.objects.make_quiz(id=id, dont_repeat = request.session['dont_repeat'])
	context = {
		'user': User.objects.get(id=request.session['user_id']),
		'questions': trivia['quiz']
	}
	request.session['dont_repeat'] = trivia['dont_repeat']
	print(request.session['dont_repeat'])
	return render(request, 'quiz/take_quiz.html', context)

def submit_quiz(request, id):
	if 'user_id' not in request.session:
		return redirect('/')
	Quiz.objects.create(
		score = id,
		user = User.objects.get(id=request.session['user_id']),
		category = Category.objects.get(id = request.session['cat_id']),
		)
	sleep(1.5)
	if 'quiz_counter' not in request.session:
		request.session['quiz_counter'] = 1
	if request.session['quiz_counter'] < 5:
		request.session['quiz_counter']+=1
		return redirect('/quiz/' + str(request.session['cat_id']))
	request.session['quiz_counter'] = 0
	return redirect('/quiz/quiz_stats')

def quiz_end(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context = {
		'user': User.objects.get(id=request.session['user_id']),
	}
	request.session['dont_repeat'] = []
	return render(request, 'quiz/quiz_end.html', context)

def quiz_stats(request):
	if 'user_id' not in request.session:
		return redirect('/')
	userlist = User.objects.all()
	leader_boardlist = []

	# this is where the divide zero bug is happening
	# my gut thinks this is because session is somehow getting dropped - more testing...
	# if Quiz.objects.filter(user = user) is null: or something...

	for user in userlist:
		if len(Quiz.objects.filter(user = user)) == 0:
			continue
		else:
			boardstats = [user.alias, 
				len(Quiz.objects.filter(user = user, score= '1')),
				len(Quiz.objects.filter(user = user)),
				int(100*len(Quiz.objects.filter(user= user, score= '1')) / len(Quiz.objects.filter(user = user))) ]
			leader_boardlist.append(boardstats)

	leader_boardlist.sort(key=lambda x: x[1])
	leader_boardlist = leader_boardlist[::-1]
	counter = 1
	for user in leader_boardlist:
		user.append(counter)
		counter += 1

	context = {
		'leaderboard': leader_boardlist,
		'user': User.objects.get(id=request.session['user_id']),
		}

	return render(request, 'quiz/quiz_chart_test.html', context)

def make_chart (request):
	return Quiz.objects.make_chart(request.session['user_id'])

def last_quiz (request):
    return Quiz.objects.last_quiz(request.session['user_id'])