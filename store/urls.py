from django.contrib import admin
from django.urls import path
from .views import index , Signup ,Login
urlpatterns = [
    #if "" string is empty then call the index method which prestent in views file
    path('', index,name='homepage'),
    path('signup', Signup.as_view()),
    path('login',Login.as_view())
]