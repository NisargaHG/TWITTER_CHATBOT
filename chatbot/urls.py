from django.urls import path
from .views import chatbot_ui

urlpatterns = [
    path('', chatbot_ui, name='chatbot_ui'),
]
