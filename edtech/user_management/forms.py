from django import forms
from django.forms import ValidationError

from .models import UserProfile, Address
from django.contrib.auth.models import User


class UserRegisterationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name',  'last_name', 'email', 'password')

    def __init__(self, *args, **kwagrs):
        super(UserRegisterationForm, self).__init__(*args, **kwagrs)

    def clean_email(self):
        email = self.cleaned_data['email']

        if not email.endswith('@gmail.com'):
            raise ValidationError('Domain of email is not valid')

        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists.')

        return email

    
class  AddressRegisterationForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('address1', 'address2', 'city', 'zipcode', 'district',  'state', 'country')

    def __init__(self, *args, **kwagrs):
        super(AddressRegisterationForm, self).__init__(*args, **kwagrs)
    
    

class UserLoginForm(forms.Form):

    class Meta:
        fields = ('username', 'password')

    def __init__(self, *args, **kwagrs):
        super(UserLoginForm, self).__int__(*args, **kwagrs)



    