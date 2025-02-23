from ast import Load
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from lead.forms import LeadForm, CustomSinginForm
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
        queryset = Lead.objects.select_related('agent','agent__user')
        
        if user.is_organisation:
            queryset = queryset.filter(organisation = user.profile)
        else:
            queryset = queryset.filter(organisation = user.agent.organisation)
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
        return Lead.objects.filter(organisarion = user.organisation)