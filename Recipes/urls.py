from django.contrib import admin
from django.urls import path
from .views import Recipe_list , Recipe_Detail

urlpatterns = [
    path('', Recipe_list.as_view(), name='Recipe_list'),
    path('/<int:pk>/', Recipe_Detail.as_view(), name='Recipe_detail'),
]