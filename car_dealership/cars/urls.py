from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_most_recent_paginated, name='index'),
    path('<int:car_id>/', views.get_car_by_id, name='car'),
    path('form/<str:form_type>/', views.admin_forms, name='admin_forms'),
    path('edit/<int:car_id>/', views.edit_car, name='edit_car'),
    path('car/delete_image/<int:image_id>/',
         views.delete_car_image, name='delete_car_image'),

]
