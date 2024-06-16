#Maps URL patterns to views. This file defines how URLs should be routed to specific views within app app.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),  # connected to views
    path('record/<int:pk>/', views.customer_record, name="record"),
    path('deleteRecord/<int:pk>/', views.delete_record, name="deleteRecord"),
    # for primary key - Will look like localhost:8000/record/1
    path('addrecord/', views.add_record, name="add_record"),
    path('updateRecord/<int:pk>/', views.update_record, name="update_record"),
]

#3 step process for creating homepage
# 1) html page, url and then a view