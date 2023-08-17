from django.urls import path
from .views import *



urlpatterns = [
    path('signup', user_signup, name='signup'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout')
]