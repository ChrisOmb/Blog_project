from django.urls import path
from .import views

urlpatterns = [
    path("", views.post_create, name='home_view'),
    path("/detail", views.post_detail, name='post_detail'),
    path("/list", views.post_list, name='post_list'),
    path("/update", views.post_update, name='post_delete'),
    path("/delete", views.post_delete, name='post_delete'),
]