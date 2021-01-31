from django.contrib import admin
from django.urls import path
from .views import index , signup ,Login
urlpatterns = [
    #if "" string is empty then call the index method which prestent in views file
    path('', index,name='homepage'),
    path('signup', signup),
    path('login',Login.as_view())
]