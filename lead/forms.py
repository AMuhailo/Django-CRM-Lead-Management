from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import Lead

User = get_user_model()

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = ['agent']
        

class CustomSinginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
        field_classes = {'username':UsernameField}