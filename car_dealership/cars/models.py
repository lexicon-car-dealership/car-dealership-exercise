from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    established_date = models.DateField()

    def __str__(self):
        return self.name

class BrandModel(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.manufacturer.name} {self.name} ({self.year})"

class Car(models.Model):
    PETROL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    CAR_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Truck', 'Truck'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Hatchback', 'Hatchback'),
        ('Van', 'Van'),
        ('Wagon', 'Wagon'),
    ]

    GEAR_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]

    model_name = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    petrol_type = models.CharField(
        max_length=10, choices=PETROL_CHOICES, default='Petrol')
    car_type = models.CharField(
        max_length=12, choices=CAR_TYPE_CHOICES, default='Sedan')
    gear_type = models.CharField(
        max_length=10, choices=GEAR_CHOICES, default='Manual')

    def __str__(self):
        return f"{self.manufacturer.name} {self.model_name} ({self.year})"


