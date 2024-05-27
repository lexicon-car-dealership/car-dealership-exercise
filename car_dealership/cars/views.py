from django.contrib import messages
from .forms import ManufacturerForm, BrandModelForm, CarForm, CarImagesForm
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models


def index(request):
    return render(request, 'index.html')


def get_car_by_id(request, car_id):
    car = get_object_or_404(
        models.Car.objects.prefetch_related('carimages_set'), id=car_id)
    car_images = car.carimages_set.all()
    return render(request, 'car_detail.html', {'car': car, 'car_images': car_images})



def get_most_recent_paginated(request):
    brand_filter = request.GET.get('brand', None)
    model_filter = request.GET.get('model', None)
    fuel_filter = request.GET.get('fuel', None)
    year_filter = request.GET.get('year', None)
    min_price_filter = request.GET.get('minPrice', None)
    max_price_filter = request.GET.get('maxPrice', None)
    filters = {}
    if brand_filter:
        filters['model_name__manufacturer__name__iexact'] = brand_filter
    if model_filter:
        filters['model_name__name__iexact'] = model_filter
    if fuel_filter:
        filters['petrol_type'] = fuel_filter
    if year_filter:
        filters['year'] = year_filter
    if min_price_filter:
        filters['price__gte'] = min_price_filter
    if max_price_filter:
        filters['price__lte'] = max_price_filter
    cars = models.Car.objects.filter(**filters).order_by('created_at')
    paginator = Paginator(cars, 10)
    page = request.GET.get('page', 1)
    try:
        cars_page = paginator.page(page)
    except PageNotAnInteger:
        cars_page = paginator.page(1)
    except EmptyPage:
        cars_page = paginator.page(paginator.num_pages)

    params = request.GET.copy()
    return render(request, 'index.html', {'cars': cars_page, 'page_obj': cars_page, 'params': params})


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
