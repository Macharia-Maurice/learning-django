from django.urls import path
from . import views
urlpatterns=[
    path('hello2/', views.greetings2)
]