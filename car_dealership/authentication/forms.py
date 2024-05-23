from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff',
                  'is_superuser', 'groups', 'user_permissions']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'user_permissions': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # If the user is not a staff member, hide the staff and superuser fields
        if user and not user.is_staff:
            self.fields['is_staff'].widget = forms.HiddenInput()
            self.fields['is_superuser'].widget = forms.HiddenInput()
            self.fields['groups'].widget = forms.HiddenInput()
            self.fields['user_permissions'].widget = forms.HiddenInput()
