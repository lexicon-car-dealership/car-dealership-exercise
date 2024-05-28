from django.forms.widgets import ClearableFileInput
from django import forms
from .models import Manufacturer, BrandModel, Car, CarImages


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        single_file_clean = super(MultipleFileField, self).clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d, initial) for d in data]
        else:
            return single_file_clean(data, initial)


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name']


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = BrandModel
        fields = ['manufacturer', 'name']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model_name', 'year', 'price', 'description',
                  'petrol_type', 'car_type', 'gear_type']


class CarImagesForm(forms.ModelForm):
    image = MultipleFileField()

    class Meta:
        model = CarImages
        fields = ['car', 'image']

    def __init__(self, *args, **kwargs):
        car = kwargs.pop('car', None)
        super().__init__(*args, **kwargs)
        if car:
            self.fields['car'].initial = car
        # Hide the car field in the form
        self.fields['car'].widget = forms.HiddenInput()


class CarWithImagesForm(forms.ModelForm):
    images = MultipleFileField(required=False)

    class Meta:
        model = Car
        fields = ['model_name', 'year', 'price', 'description',
                  'petrol_type', 'car_type', 'gear_type', 'images']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.attrs.update({'multiple': True})
