from django import forms
from lead.models import Agent
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class AgentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']
        widgets = {
            'username':forms.TextInput(attrs={
                "class":"form-control"
            }),
            'first_name':forms.TextInput(attrs={
                "class":"form-control"
            }),
            'last_name':forms.TextInput(attrs={
                "class":"form-control"
            }),
            'email':forms.EmailInput(attrs={
                "class":"form-control"
            }),
        }