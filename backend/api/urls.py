from django.urls import path
from . import views

urlpatterns = [
    path("foods/", views.get_foods),
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
]
