from django.urls import path
from simple_chatbot.views import SimpleChatbot

urlpatterns = [
    path("simple_chatbot/", SimpleChatbot.as_view())
]