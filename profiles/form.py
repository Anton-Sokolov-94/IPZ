import django.forms

from django import forms
from registration.forms import RegistrationFormUniqueEmail
from profiles.models import UserProfile



class ProfileForm(django.forms.ModelForm):
  class Meta:
      model = UserProfile
      exclude = ('user','last_name',)



CHOICES=[('0','Lector'),
         ('1','Student')]

class RegistrationFormProfile(RegistrationFormUniqueEmail):
    user_type = forms.ChoiceField(choices=CHOICES, label = 'Status')
