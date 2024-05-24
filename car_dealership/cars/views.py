from django.shortcuts import get_object_or_404, render, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models

def index(request):
    return render(request, 'index.html')

def get_car_by_id(request, car_id):
    car = get_object_or_404(models.Car, pk=car_id)
    return HttpResponse(car)


def get_most_recent_paginated(request):
    cars = models.Car.objects.all()
    cars.order_by('created_at')
    paginator = Paginator(cars, 10)
    page = request.GET.get('page', 1)
    try:
        cars_page = paginator.page(page)
    except PageNotAnInteger:
        cars_page = paginator.page(1)
    except EmptyPage:
        cars_page = paginator.page(paginator.num_pages)

    return HttpResponse(cars_page)

