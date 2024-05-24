from faker import Faker
from vehicle_faker import VehicleProvider
from cars.models import Car, BrandModel, Manufacturer
from vehicle_dict import vehicles


def seed_db():
    fake = Faker()
    fake.add_provider(VehicleProvider)

    manuf_list = set([v['manufacturer_name'] for v in vehicles])

    for m in manuf_list[0]:
        mf = Manufacturer(name=m)
        mf.save()
        manufacturer_models = list(set([i['model_name'] for i in list(
            filter(lambda x: x['manufacturer_name'] == m, vehicles))]))

        for model in manufacturer_models[0]:

            mdl = BrandModel(manufacturer=mf, name=model)
            mdl.save()
            # cars = list(filter(lambda x: x['manufacturer_name'] == m and x['model_name'] == model,  vehicles))
            for _c in range(5):

                car_dict = fake.vehicle_object_dict()

                c = Car(model_name=mdl, year=1111, **car_dict)
                c.save()


if __name__ == '__main__':
    seed_db()
