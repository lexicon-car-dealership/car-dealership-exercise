from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_most_recent_paginated, name='cars'),
    path('<int:car_id>/', views.get_car_by_id, name='car'),
]
