from django.urls import path
from . import views


urlpatterns = [

path('addpublisher', views.addpublisher,name='addpublisher'),
path('booklist', views.booklist,name='booklist'),


]