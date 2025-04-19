from django.urls import path

from pages import views

from .api_views import api_home  # Import the api_home function

urlpatterns = [
    path("api/", api_home, name="api_home"),  # Map the API endpoint
    path("", views.home, name="home"),
]
