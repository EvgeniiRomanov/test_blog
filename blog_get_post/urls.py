
from django.urls import path, include
from . import views     # . значит с данного приложения, за его пределы не лезем

urlpatterns = [
    path('blogs/', views.BlogAPIView.as_view()),
]
