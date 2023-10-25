from django.urls import path,include
from Chatbot import views


urlpatterns = [
  
    path('webhook/', views.webhook, name ='webhook'),
]
