from ast import Load
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView
from lead.forms import LeadForm, CustomSinginForm, AssignAgentForm
from lead.models import Lead, Agent
# Create your views here.

class EditFormMixin:
    model = Lead
    form_class = LeadForm
    success_url = reverse_lazy('lead:lead_list_url')
    
    
class SelectedMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["select"] = 'lead'
        return context
    
class LeadTypeFilterMixin:
    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.select_related('agent','agent__user','category')
        
        if user.is_organisation:
            queryset = queryset.filter(organisation = user.profile, agent__isnull = False)
        else:
            queryset = queryset.filter(organisation = user.agent.organisation, agent__isnull = False)
            queryset = queryset.filter(agent__user = user)
        return queryset
    

class SinginView(CreateView):
    template_name = 'registration/singin.html'
    form_class = CustomSinginForm
    success_url = reverse_lazy("login")
    
    
class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    
    
class LeadListView(LoginRequiredMixin, LeadTypeFilterMixin ,SelectedMixin, ListView):
    model = Lead
    context_object_name = 'leads'
    template_name = 'lead/lead_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisation:
            context["unassigned_leads"] = Lead.objects.filter(agent__isnull = True).select_related('agent','agent__user','category')
        return context
    
    

class LeadDetailView(LoginRequiredMixin, LeadTypeFilterMixin, SelectedMixin, DetailView):
    model = Lead
    template_name = 'lead/lead_detail.html'
    context_object_name = 'lead'
    def get_object(self, queryset = ...):
        return get_object_or_404(Lead, pk=self.kwargs.get('lead_pk'))


class LeadCreateView(LoginRequiredMixin, LeadTypeFilterMixin, SelectedMixin, EditFormMixin, CreateView):
    template_name = 'lead/forms/createlead.html'
    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation = self.request.user.profile
        lead.save()
        return super().form_valid(form)
    

class LeadUpdateView(LoginRequiredMixin, SelectedMixin, EditFormMixin, UpdateView):
    pk_url_kwarg = 'lead_pk'
    template_name = 'lead/forms/updatelead.html'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation = user.is_organisation)
    

        
class AssignLeadAgent(LoginRequiredMixin, SelectedMixin, FormView):
    template_name = 'lead/forms/assignlead.html'
    form_class = AssignAgentForm
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs.update(
            {"user":self.request.user}
        )
        return kwargs

    def get_success_url(self):
        return reverse_lazy('lead:lead_list_url')
    
    
    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(id = self.kwargs.get('lead_pk'))
        lead.agent = agent
        lead.save()
        return super().form_valid(form)

        