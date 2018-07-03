from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login.models import User
from apps.quiz.models import Quiz


# landing page
def index(request):
    page = None
    if 'hero' not in request.session:
        request.session['hero'] = 'show'
    if 'user_id' not in request.session:
        request.session['status'] = 'guest'
        page = render(request, 'login/login.html')
    else:
        request.session['status'] = 'logged_in'
        current_user = User.objects.get(id=request.session['user_id'])
        page = render(request, 'login/login.html', {'user': current_user})

    return page


# register new user
def register(request):
    result = User.objects.validate_registration(request.POST)
    if result['status'] is not True:
        for error in result['errors']:
            messages.error(request, result['errors'][error])
            request.session['hero'] = 'hide'
        return redirect('/')
    else:
        request.session['user_id'] = result['user_id']
        return redirect('/quiz')


# log in existing user
def login(request):
    result = User.objects.validate_login(request.POST)
    if result['status'] is not True:
        for error in result['errors']:
            messages.error(request, result['errors'][error])
            request.session['hero'] = 'hide'
        return redirect('/')
    else:
        request.session['user_id'] = result['user_id']
        return redirect('/quiz')


# clear request.session data
def logout(request):
    request.session.flush()
    return redirect('/')


def account_info(request):
    if 'user_id' not in request.session:
        return redirect('/')
    current_user = User.objects.get(id=request.session['user_id'])
    return render(request, 'login/user_account.html', {'user': current_user})


def credits(request):
    current_user = User.objects.get(id=request.session['user_id'])
    return render(request, 'login/credits.html', {'user': current_user})


def bar_data(request):
    return Quiz.objects.bar_data(request.session['user_id'])
