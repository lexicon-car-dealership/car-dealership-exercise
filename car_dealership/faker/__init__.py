from faker import Faker
from vehicle_faker import VehicleProvider
fake = Faker()
fake.add_provider(VehicleProvider)

print(fake.vehicle_generated_vin())
print(fake.vehicle_year_make_model_cat_vin())