from django import forms
from lead.models import Agent

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['user']