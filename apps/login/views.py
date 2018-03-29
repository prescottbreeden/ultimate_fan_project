from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from apps.login.models import User
from .models import User


# landing page
def index(request):
	if 'user_id' not in request.session:
		request.session['status'] = 'guest'
		return render(request, 'login/login.html')
	else:
		request.session['status'] = 'logged_in'
		return render(request, 'login/login.html', {'user': User.objects.get(id=request.session['user_id'])})

# register new user
def register(request):
	result = User.objects.validate_registration(request.POST)
	if result['status'] != True:
		for error in result['errors']:
			messages.error(request, result['errors'][error])
		return redirect('/')
	else:
		request.session['user_id'] = result['user_id']
		return redirect('/')

# log in existing user
def login(request):
	result = User.objects.validate_login(request.POST)
	if result['status'] != True:
		for error in result['errors']:
			messages.error(request, result['errors'][error])
		return redirect('/')
	else:
		request.session['user_id'] = result['user_id']
		return redirect('/')

# clear request.session data
def logout(request):
	request.session.flush()
	return redirect('/')

def account_info(request):
	if 'user_id' not in request.session:
		return redirect('/')
	return render(request, 'login/user_account.html')