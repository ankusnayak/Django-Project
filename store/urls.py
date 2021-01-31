from django.contrib import admin
from django.urls import path
from .views import home,login,signup

urlpatterns = [
    #if "" string is empty then call the index method which prestent in views file
    path('', home.index,name='homepage'),
    path('signup', signup.Signup.as_view(),name='signup'),
    path('login',login.Login.as_view(),name='login')
]