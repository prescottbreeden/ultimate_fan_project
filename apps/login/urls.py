from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('account', views.account_info, name='account_info'),
    path('bar_data', views.bar_data, name='bar_data'),
    ]
