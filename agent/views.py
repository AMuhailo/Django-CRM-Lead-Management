from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from agent.forms import AgentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from lead.models import Agent

# Create your views here.
class EditAgentMixin:
    model = Agent
    form_class = AgentForm
    success_url = reverse_lazy('agent:agent_list_url')
    
class FilterAgentMixin:
    def get_queryset(self):
        organisation = self.request.user.profile
        return Agent.objects.filter(organisation=organisation)    

class AgentListView(LoginRequiredMixin, FilterAgentMixin, ListView):
    model= Agent
    context_object_name = 'agents'
    template_name = 'agent/agent_list.html'

class AgentDetailView(LoginRequiredMixin, FilterAgentMixin, DetailView):
    model = Agent
    context_object_name = 'agent'
    pk_url_kwarg = 'agent_pk'
    template_name = 'agent/agent_detail.html'
    
    
class AgentCreateView(LoginRequiredMixin, EditAgentMixin, FilterAgentMixin, CreateView):
    template_name = 'agent/forms/createagent.html'
    def form_valid(self, form):
        agent = form.save(commit = False)
        agent.organisation = self.request.user.profile
        agent.save()
        return super().form_valid(form)
    
class AgentUpdateView(LoginRequiredMixin, EditAgentMixin, FilterAgentMixin, UpdateView):
    pk_url_kwarg = 'agent_pk'
    template_name = 'agent/forms/updateagent.html'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    