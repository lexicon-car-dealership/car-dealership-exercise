import json
import urllib.request
from seed_faker.vehicle_faker import VehicleProvider
from faker import Faker
from cars.models import Car, BrandModel, Manufacturer
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_dealership.settings')

print('Seeding process started ..')
django.setup()


def seed_db():
    fake = Faker()
    fake.add_provider(VehicleProvider)

    manuf_list = get_manufacturers_names_list()

    for m in manuf_list:
        mf = Manufacturer(name=m)

        mf.save()
        manufacturer_models = get_model_names_by_manufacturer(m)
        for model in manufacturer_models:

            mdl = BrandModel(manufacturer=mf, name=model)
            mdl.save()

            car_dict = fake.vehicle_object_dict()
            c = Car(model_name=mdl,  **car_dict)
            c.save()
            print(f'Saving {m} {mdl} ...')


def fast_seed():
    fake = Faker()
    fake.add_provider(VehicleProvider)

    manuf_list = list(get_manufacturers_names_list())

    manufacturers = []
    brand_models = []
    cars = []

    # Collect manufacturers
    for m in manuf_list:
        manufacturer, created = Manufacturer.objects.get_or_create(name=m)
        if created:
            manufacturers.append(manufacturer)

    # Bulk create manufacturers
    Manufacturer.objects.bulk_create(manufacturers)
    print(f'Bulk creation of manufactures done, count = {len(manufacturers)}')

    # Fetch saved manufacturers from DB
    saved_manufacturers = {mf.name: mf for mf in Manufacturer.objects.all()}
    print(f'Saved manufactures count  = {len(saved_manufacturers)}')

    # Collect models and cars
    for m in manuf_list:
        mf = saved_manufacturers[m]
        manufacturer_models = get_model_names_by_manufacturer(m)
        for model in manufacturer_models:
            mdl = BrandModel(manufacturer=mf, name=model)
            brand_models.append(mdl)

    # Bulk create brand models
    BrandModel.objects.bulk_create(brand_models)

    # Fetch saved brand models from DB
    saved_models = {mdl.name: mdl for mdl in BrandModel.objects.all()}

    # Create cars
    for i, mdl in enumerate(saved_models.values()):
        if i >= 100:
            break
        for _ in range(1):  # Adjust the number of cars per model
            car_dict = fake.vehicle_object_dict()
            c = Car(model_name=mdl, **car_dict)
            cars.append(c)
            print(f'Appending {mdl}')

    # Bulk create cars
    print('Bulk create cars')
    Car.objects.bulk_create(cars)

    print('All data has been saved successfully.')


def get_model_names_by_manufacturer(manufacturer):
    newurl = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{manufacturer.split(' ')[0]}?format=json"
    print(newurl)
    with urllib.request.urlopen(newurl) as url:
        return set([v['Model_Name'] for v in json.load(url)['Results']])


def get_manufacturers_names_list():
    with urllib.request.urlopen("https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/car?format=json") as url:
        return set([v['MakeName'] for v in json.load(url)['Results']])


if __name__ == '__main__':
    fast_seed()
