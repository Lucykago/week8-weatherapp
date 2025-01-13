from django.urls import path
from . import views  # Import the views from your app

urlpatterns = [
    path('', views.home, name='home'),  # This is the URL pattern for the home view
]
