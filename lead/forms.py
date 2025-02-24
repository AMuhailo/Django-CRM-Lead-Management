from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import Category, Lead,Agent

User = get_user_model()

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = ['organisation','category']
        widgets = {
            'first_name':forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"First name",                
            }),
            'last_name':forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Last name",                
            }),
            'email':forms.EmailInput(attrs={
                "class":"form-control",
                "placeholder":"test@gmail.com",                
            }),
            'phone':forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"000-1234-123",                
            }),
            'age':forms.NumberInput(attrs={
                "class":"form-control",
                "placeholder":"18+",                
            }),
            'agent':forms.Select(attrs={
                "class":"form-select",
            }),
            }

class CustomSinginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
        field_classes = {'username':UsernameField}
    

class CategoryLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['category']
        widgets = {"category":forms.Select(attrs={
            'class':'form-select my-3',
            "id":"floatingSelect",
        })}

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())
    
    def __init__(self,*args, **kwargs):
        user = kwargs.pop('user')
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = Agent.objects.filter(organisation=user.profile)