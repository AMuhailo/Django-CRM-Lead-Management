from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import Category, Lead,Agent

User = get_user_model()

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = ['organisation','category']
        

class CustomSinginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
        field_classes = {'username':UsernameField}
    

class CategoryLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['category']

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())
    
    def __init__(self,*args, **kwargs):
        user = kwargs.pop('user')
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = Agent.objects.filter(organisation=user.profile)