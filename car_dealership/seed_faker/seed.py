from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from faker import Faker
from vehicle_faker import VehicleProvider
from cars.models import Car, BrandModel, Manufacturer
import urllib.request
import json


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

            for _c in range(5):
                car_dict = fake.vehicle_object_dict()
                c = Car(model_name=mdl, year=1111, **car_dict)
                c.save()
                print(f'in progress.. {m} {mdl}')


def get_model_names_by_manufacturer(manufacturer):
    with urllib.request.urlopen(f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{manufacturer}?format=json") as url:
        return set([v['Model_Name'] for v in json.load(url)['Results']])


def get_manufacturers_names_list():
    with urllib.request.urlopen("https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/car?format=json") as url:
        return set([v['MakeName'] for v in json.load(url)['Results']])


if __name__ == '__main__':
    seed_db()
