from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .forms import ManufacturerForm, BrandModelForm, CarForm, CarImagesForm
from django.contrib import messages

from . import models


def index(request):
    return render(request, 'index.html')


def get_car_by_id(request, car_id):
    car = get_object_or_404(
        models.Car.objects.prefetch_related('carimages_set'), id=car_id)
    car_images = car.carimages_set.all()
    return render(request, 'car_detail.html', {'car': car, 'car_images': car_images})



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
    models_list = []
    if brandFilter:
        models_list = models.Car.objects.filter(model_name__manufacturer__name=brandFilter).values_list(
            'model_name__name', flat=True).distinct()

    params = request.GET.copy()
    return render(request, 'index.html', {'cars': cars_page, 'brands': unique_brands, 'models': models_list, 'page_obj': cars_page, 'params': params})

def admin_forms(request, form_type):
    form_map = {
        'manufacturer': ManufacturerForm,
        'brandmodel': BrandModelForm,
        'car': CarForm,
        'carimages': CarImagesForm,
    }

    if request.method == 'POST':
        if form_type == 'carimages':
            form = CarImagesForm(request.POST, request.FILES)
            if form.is_valid():
                car = form.cleaned_data['car']
                images = form.cleaned_data['image']
                for image in images:
                    models.CarImages.objects.create(car=car, image=image)
                messages.success(
                    request, 'Car images uploaded successfully.')
                return redirect('index')
            else:
                print(form.errors)
                messages.error(
                    request, 'Form is not valid. Please check the fields.')
        else:
            form = form_map[form_type](request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(
                    request, f'{form_type.capitalize()} saved successfully.')
                return redirect('index')
            else:
                print(form.errors)
                messages.error(
                    request, 'Form is not valid. Please check the fields.')
    else:
        form = form_map[form_type]()

    return render(request, 'forms/admin.html', {'form': form})
