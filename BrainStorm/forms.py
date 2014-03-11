from django import forms
from BrainStorm.models import Session
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class SessionForm(forms.ModelForm):

    class Meta:
        model = Session