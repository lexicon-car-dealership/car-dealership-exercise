
from .models import Manufacturer, BrandModel, Car, CarImages, Reservation
from .forms import EditCarForm, ManufacturerForm, BrandModelForm, CarForm, CarImagesForm, AddCarForm
from django.shortcuts import render, redirect, get_object_or_404
import os
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import models


def car_detail(request, car_id):
    car = get_object_or_404(
        models.Car.objects.prefetch_related('carimages_set'), id=car_id)
    car_images = car.carimages_set.all().order_by('-featured')

    similar_cars = models.Car.objects.filter(model_name=car.model_name).exclude(
        id=car_id).prefetch_related('carimages_set')

    for similar_car in similar_cars:
        featured_image = similar_car.carimages_set.filter(
            featured=True).first()
        similar_car.featured_image = featured_image
    user = request.user
    if user.is_authenticated:
        reservation = Reservation.objects.filter(user=user, car=car).first()
    return render(request, 'car/car_detail.html', {'car': car, 'car_images': car_images, 'similar_cars': similar_cars[:4], 'reservation': reservation})


def index(request):
    brand_filter = request.GET.get('brand', None)
    model_filter = request.GET.get('model', None)
    fuel_filter = request.GET.get('fuel', None)
    year_filter = request.GET.get('year', None)
    min_price_filter = request.GET.get('minPrice', None)
    max_price_filter = request.GET.get('maxPrice', None)
    search_query = request.GET.get('search', None)

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
    cars = models.Car.objects.filter(
        **filters).prefetch_related('carimages_set')
    if search_query:
        cars = cars.filter(
            Q(model_name__name__icontains=search_query) |
            Q(model_name__manufacturer__name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    cars = cars.order_by('-created_at')
    paginator = Paginator(cars, 10)
    page = request.GET.get('page', 1)
    try:
        cars_page = paginator.page(page)
    except PageNotAnInteger:
        cars_page = paginator.page(1)
    except EmptyPage:
        cars_page = paginator.page(paginator.num_pages)

    for car in cars_page:
        featured_image = car.carimages_set.filter(featured=True).first()
        car.featured_image = featured_image

    unique_brands = models.Car.objects.values_list(
        'model_name__manufacturer__name', flat=True).distinct()
    models_list = []
    if brand_filter:
        models_list = models.Car.objects.filter(model_name__manufacturer__name=brand_filter).values_list(
            'model_name__name', flat=True).distinct()

    params = request.GET.copy()
    return render(request, 'index.html', {'cars': cars_page, 'brands': unique_brands, 'models': models_list, 'page_obj': cars_page, 'params': params})


def get_additional_form_data(form):
    if form == 'manufacturer':
        return [i.name for i in Manufacturer.objects.all()], None

    if form == 'brandmodel':
        brandmodels = BrandModel.objects.all()
        manufacturers = Manufacturer.objects.all()  # corrected to return queryset
        return brandmodels, manufacturers
    return [], None


def admin_forms(request, form_type):
    form_map = {
        'manufacturer': ManufacturerForm,
        'brandmodel': BrandModelForm,
        'car': CarForm,
        'carimages': CarImagesForm,
    }
    form_name_map = {
        'manufacturer': 'Manufacturer',
        'brandmodel': 'Brand Model',
        'car': 'Add Car',
        'carimages': 'Car Images',
    }

    form_name = form_name_map.get(form_type, 'Admin Form')
    form_class = form_map.get(form_type)

    if not form_class:
        messages.error(request, 'Invalid form type.')
        return redirect('index')

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            if form_type == 'carimages':
                car = form.cleaned_data['car']
                images = form.cleaned_data['image']
                for image in images:
                    CarImages.objects.create(car=car, image=image)
                messages.success(request, 'Car images uploaded successfully.')
            elif form_type == 'brandmodel':
                brand_model = form.save(commit=False)
                manufacturer = form.cleaned_data['manufacturer']
                brand_model.manufacturer = manufacturer
                brand_model.save()
                messages.success(request, 'Brand Model saved successfully.')
            else:
                form.save()
                messages.success(request, f'{form_name} saved successfully.')
            return redirect('admin_forms', form_type=form_type)
        else:
            messages.error(
                request, 'Form is not valid. Please check the fields.')
    else:
        form = form_class()
    data, manufacturers = get_additional_form_data(form_type)
    context = {'form': form, 'form_name': form_name, 'data': data}
    if manufacturers:
        context['manufacturers'] = manufacturers
    return render(request, 'forms/admin_forms.html', context)


def edit_car(request, car_id):
    car = get_object_or_404(models.Car, id=car_id)
    if request.method == 'POST':
        car_form = EditCarForm(request.POST, request.FILES, instance=car)

        if car_form.is_valid():
            car = car_form.save()
            has_featured_image = car.carimages_set.filter(
                featured=True).exists()

            images = request.FILES.getlist('images')
            for i, image in enumerate(images):
                if not has_featured_image and i == 0:
                    models.CarImages.objects.create(
                        car=car, image=image, featured=True)
                else:
                    models.CarImages.objects.create(
                        car=car, image=image)

            featured_image_id = request.POST.get('featured_image')
            if featured_image_id:
                # Unset previously featured images
                CarImages.objects.filter(
                    car=car, featured=False).update(featured=False)
                # Set new featured image
                featured_image = CarImages.objects.get(id=featured_image_id)
                featured_image.featured = True
                featured_image.save()

            messages.success(request, 'Car details updated successfully.')
            return redirect('car', car_id=car.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        car_form = EditCarForm(instance=car)

    car_images = car.carimages_set.all()
    return render(request, 'car/edit_car.html', {
        'car_form': car_form,
        'car_images': car_images,
        'car': car
    })


def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST, request.FILES)

        if form.is_valid():
            brand_model_name = form.cleaned_data['brand_model_name']
            images = request.FILES.getlist('images')

            car = form.save(commit=False)
            car.model_name = brand_model_name
            car.save()

            # Handle Images
            for i, image in enumerate(images):
                CarImages.objects.create(
                    car=car, image=image, featured=True if i == 0 else False)

            messages.success(request, 'Car added successfully.')
            return redirect('car', car_id=car.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AddCarForm()

    return render(request, 'car/add_car.html', {'form': form})


def delete_car_image(request, image_id):
    image = get_object_or_404(models.CarImages, id=image_id)
    car = image.car
    car_id = car.id
    image_path = image.image.path

    if request.method == 'POST':
        featured = image.featured
        image.delete()
        if featured:
            has_images = car.carimages_set.all()
            if len(has_images) > 0:
                has_images[0].featured = True
                has_images[0].save()
        # Delete the image file
        if os.path.isfile(image_path):
            try:
                os.remove(image_path)
            except Exception as e:
                messages.error(request, f'Error deleting image file: {e}')
                return redirect('edit_car', car_id=car_id)

        # Check if there are any remaining images for the car
        remaining_images = models.CarImages.objects.filter(car=car).exists()

        # If no images are left, remove the directory
        if not remaining_images:
            car_image_directory = os.path.dirname(image_path)
            try:
                os.rmdir(car_image_directory)
                messages.success(
                    request, 'Image and directory deleted successfully.')
            except Exception as e:
                messages.error(request, f'Error deleting directory: {e}')
        else:
            messages.success(request, 'Image deleted successfully.')

    return redirect('edit_car', car_id=car_id)


@login_required
def reserve_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        existing_reservation = Reservation.objects.filter(
            user=request.user, car=car).exists()
        if existing_reservation:
            messages.error(request, 'You have already reserved this car.')
        else:
            reservation = Reservation.objects.create(
                user=request.user, car=car)
            reservation.save()
            messages.success(request, 'Car reserved successfully!')

        return redirect('car', car_id=car.id)
    return redirect('car', car_id=car.id)


@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        if reservation.user == request.user:
            reservation.delete()
            messages.success(request, 'Reservation cancelled successfully!')
        else:
            messages.error(
                request, 'You are not authorized to cancel this reservation.')
    return redirect(request.META.get('HTTP_REFERER', '/'))
