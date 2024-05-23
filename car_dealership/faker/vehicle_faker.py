import faker
from random import choice
from faker.providers import BaseProvider
from vehicle_dict import vehicles



class VehicleProvider(BaseProvider):

    """
    A Provider for vehicle related test data.

    >>> from faker import Faker
    >>> from vehicle_faker import VehicleProvider
    >>> fake = Faker()
    >>> fake.add_provider(VehicleProvider)
    

    
    vehicle_object(self):        
        Returns a random vehicle dict example:
        {"Year": 2008, "Make": "Jeep", "Model": "Wrangler", "Category": "SUV"}
    
    vehicle_year_make_model(self):
        Returns str: Year Make Model 
        example: 1997 Nissan 240SX

    vehicle_year_make_model_cat_vin(self):
        Returns str: Year Make Model Cat 
        example:
        2017 GMC Sierra 1500 Double Cab (Pickup)
        
    vehicle_make_model(self):
        Returns str: Make Model 
        example: Audi Q7

    vehicle_make(self):
        Returns str: Make 
        example: Lincoln

    vehicle_year(self):
        Returns str: Year 
        example: 1999
        

    def vehicle_model(self):
        Returns str: Model 
        example: Prius
        

    def vehicle_category(self):
        Returns str: Category 
        example: SUV
        
    def vehicle_generated_vin(self):
        Returns str: VIN
        example: 'RT3GZYSKXXNDZ9J97'
        
    

    """
   

    def vehicle_object(self):
        """
        Returns a random vehicle dict example:
        {"Year": 2008, "Make": "Jeep", "Model": "Wrangler", "Category": "SUV"}
        """
        veh = choice(vehicles)
        fake = faker.Faker()
        veh = veh|{'VIN':fake.vin()}
        return veh

    def vehicle_year_make_model(self):
        """Returns Year Make Model example: 1997 Nissan 240SX"""
        veh = self.vehicle_object()
        year = veh.get('Year')
        make = veh.get('Make')
        model = veh.get('Model')
        return str(year) + ' ' + make + ' ' + model

    def vehicle_year_make_model_cat_vin(self):
        """
        Returns Year Make Model Cat example:
        2017 GMC Sierra 1500 Double Cab (Pickup)
        """
        veh = self.vehicle_object()
        year = veh.get('Year')
        make = veh.get('Make')
        model = veh.get('Model')
        cat = veh.get('Category')
        vin = veh.get('VIN')
        return str(year) + ' ' + make + ' ' + model + ' (' + cat + ') ' + vin

    def vehicle_make_model(self):
        """Returns Make Model example: Audi Q7"""
        veh = self.vehicle_object()
        make = veh.get('Make')
        model = veh.get('Model')
        return make + ' ' + model

    def vehicle_make(self):
        """Returns Make example: Lincoln"""
        veh = self.vehicle_object()
        return veh.get('Make')

    def vehicle_year(self):
        """Returns Year example: 1999"""
        veh = self.vehicle_object()
        return str(veh.get('Year'))

    def vehicle_model(self):
        """Returns Model example: Frontier King Cab"""
        veh = self.vehicle_object()
        return veh.get('Model')

    def vehicle_category(self):
        """Returns Category example: SUV"""
        veh = self.vehicle_object()
        return veh.get('Category')

    def vehicle_generated_vin(self):
        """Returns VIN example: 'RT3GZYSKXXNDZ9J97'"""
        veh = self.vehicle_object()
        return veh.get('VIN')
    
