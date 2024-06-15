#Maps URL patterns to views. This file defines how URLs should be routed to specific views within app app.

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"), #connected to views
]

#3 step process for creating homepage
# 1) html page, url and then a view