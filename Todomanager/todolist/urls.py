from django.urls import path, include
from . import views
#Connect Urls with Views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contactus/', views.contact, name='contact'),
    path('about/', views.aboutus, name='aboutus'),
    path('todolist/', views.todolist, name='todolist'),

]