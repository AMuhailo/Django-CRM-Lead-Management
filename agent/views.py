from django.shortcuts import render
from agent.mixins import LoginMixinOrganisation
from django.urls import reverse_lazy
from agent.forms import AgentForm
from random import randint
from django.db.models import Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from lead.models import Agent

# Create your views here.
class EditAgentMixin:
    model = Agent
    form_class = AgentForm
    success_url = reverse_lazy('agent:agent_list_url')
    
class FilterAgentMixin:
    queryset = Agent.objects.select_related('user','user__profile')
    def get_queryset(self):
        organisation = self.request.user.profile
        
        return self.queryset.filter(organisation=organisation).annotate(lead_total = Count('leads')) 

class AgentListView(LoginMixinOrganisation, FilterAgentMixin, ListView):
    model= Agent
    context_object_name = 'agents'
    template_name = 'agent/agent_list.html'
    

class AgentDetailView(LoginMixinOrganisation, FilterAgentMixin, DetailView):
    model = Agent
    context_object_name = 'agent'
    pk_url_kwarg = 'agent_pk'
    template_name = 'agent/agent_detail.html'
    
    
class AgentCreateView(LoginMixinOrganisation, EditAgentMixin, FilterAgentMixin, CreateView):
    template_name = 'agent/forms/createagent.html'
    def form_valid(self, form):
        user = form.save(commit = False)
        user.is_agent = True
        user.is_organisation = False
        user.set_password(str(randint(1000,10000000)))
        user.save()
        Agent.objects.create(user = user,
                             organisation = self.request.user.profile)
        return super().form_valid(form)
    
class AgentUpdateView(LoginMixinOrganisation, EditAgentMixin, FilterAgentMixin, UpdateView):
    pk_url_kwarg = 'agent_pk'
    template_name = 'agent/forms/updateagent.html'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)    
    