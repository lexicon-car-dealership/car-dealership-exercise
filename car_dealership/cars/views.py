from django.shortcuts import get_object_or_404, render, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models

def index(request):
    return render(request, 'index.html')

def get_car_by_id(request, car_id):
    car = get_object_or_404(models.Car, pk=car_id)
    return HttpResponse(car)


def get_most_recent_paginated(request):
    brandFilter = request.GET.get('brand', None)
    modelFilter = request.GET.get('model', None)
    fuelFilter = request.GET.get('fuel', None)
    yearFilter = request.GET.get('year', None)
    minPriceFilter = request.GET.get('minPrice', None)
    maxPriceFilter = request.GET.get('maxPrice', None)
    filters = {}
    if brandFilter:
        filters['model_name__manufacturer__name__iexact'] = brandFilter
    if modelFilter:
        filters['model_name__name__iexact'] = modelFilter
    if fuelFilter:
        filters['petrol_type'] = fuelFilter
    if yearFilter:
        filters['year'] = yearFilter
    if minPriceFilter:
        filters['price__gte'] = minPriceFilter
    if maxPriceFilter:
        filters['price__lte'] = maxPriceFilter
    cars = models.Car.objects.filter(**filters)
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

