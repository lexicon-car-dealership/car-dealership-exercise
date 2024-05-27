from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

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
    search_query = request.GET.get('search', None)

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
    if search_query:
        cars = cars.filter(
            Q(model_name__name__icontains=search_query) |
            Q(model_name__manufacturer__name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    cars = cars.order_by('created_at')
    paginator = Paginator(cars, 10)
    page = request.GET.get('page', 1)
    try:
        cars_page = paginator.page(page)
    except PageNotAnInteger:
        cars_page = paginator.page(1)
    except EmptyPage:
        cars_page = paginator.page(paginator.num_pages)

    unique_brands = models.Car.objects.values_list(
        'model_name__manufacturer__name', flat=True).distinct()

    return render(request, 'index.html', {'cars': cars_page, 'brands': unique_brands})


def get_models(request):
    brand = request.GET.get('brand')
    out = models.Car.objects.filter(model_name__manufacturer__name=brand).values_list(
        'model_name__name', flat=True).distinct()
    return JsonResponse({'models': list(out)})
