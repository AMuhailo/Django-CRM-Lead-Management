from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView , DeleteView
from lead.forms import CategoryLeadForm, LeadForm, CustomSinginForm, AssignAgentForm
from lead.models import Category, Lead, Agent
from lead.tasks import send_lead_message
# Create your views here.


""" MIXIN """
class SelectedMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["select"] = 'lead'
        return context
    

class CategoryMixin(SelectedMixin):
    def get_queryset(self):
        user = self.request.user
        if user.is_organisation:
            categories = Category.objects.filter(organisation = user.profile).select_related('organisation').annotate(category_count=Count('category_leads'))
        else:
            categories = Category.objects.filter(organisation = user.agent.organisation).select_related('organisation').annotate(category_count=Count('category_leads'))
        return categories
    

class LeadTypeFilterMixin(SelectedMixin):
    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.select_related('agent','agent__user','category')
        
        if user.is_organisation:
            queryset = queryset.filter(organisation = user.profile, agent__isnull = False)
        else:
            queryset = queryset.filter(organisation = user.agent.organisation, agent__isnull = False)
            queryset = queryset.filter(agent__user = user)
        return queryset
    
    
class EditFormMixin(LeadTypeFilterMixin):
    model = Lead
    form_class = LeadForm
    success_url = reverse_lazy('lead:lead_list_url')
     
     
""" LEAD VIEW """
class SinginView(CreateView):
    template_name = 'registration/singin.html'
    form_class = CustomSinginForm
    success_url = reverse_lazy("login")
    
    
class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    
    
class LeadListView(LoginRequiredMixin, LeadTypeFilterMixin, ListView):
    model = Lead
    context_object_name = 'leads'
    template_name = 'lead/lead_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisation:
            context["unassigned_leads"] = Lead.objects.filter(agent__isnull = True).select_related('agent','agent__user','category')
        return context
    

class LeadDetailView(LoginRequiredMixin, LeadTypeFilterMixin, DetailView):
    model = Lead
    template_name = 'lead/lead_detail.html'
    context_object_name = 'lead'
    def get_object(self, queryset = ...):
        return get_object_or_404(Lead, pk=self.kwargs.get('lead_pk'))


class LeadCreateView(LoginRequiredMixin, EditFormMixin, CreateView):
    template_name = 'lead/forms/createlead.html'
    success_url = reverse_lazy('lead:lead_list_url')
    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation = self.request.user.profile
        lead.save()
        send_lead_message.delay(lead.id)
        return super().form_valid(form)
    

class LeadUpdateView(LoginRequiredMixin, EditFormMixin, UpdateView):
    template_name = 'lead/forms/updatelead.html'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_object(self, queryset = ...):
        lead = Lead.objects.select_related('organisation__user','organisation')
        return get_object_or_404(lead, id = self.kwargs.get('lead_pk'))
    
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation = user.is_organisation)
    
class LeadDeleteView(LoginRequiredMixin, LeadTypeFilterMixin, DeleteView):
    model = Lead
    template_name = 'lead/deletelead.html'
    pk_url_kwarg = 'lead_pk'
    success_url = reverse_lazy('lead:lead_list_url')
    
""" CATEGORY """
class CategoryListView(LoginRequiredMixin, CategoryMixin, ListView):
    template_name = 'lead/category_list.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["unassigned"] = Lead.objects.filter(agent__isnull = True).count()
        return context
    

class CategoryDetailView(LoginRequiredMixin, CategoryMixin, DetailView):
    model = Category
    template_name = 'lead/category_detail.html'
    context_object_name = 'category'

    def get_object(self, queryset = ...):
        queryset = Category.objects.prefetch_related('category_leads__agent','category_leads__agent__user')
        return get_object_or_404(queryset, title = self.kwargs.get('category_title'))
    

class CategoryLeadUpdateView(LoginRequiredMixin, CategoryMixin, UpdateView):
    form_class = CategoryLeadForm
    template_name = 'lead/forms/categoryupdatelead.html'
    
    def get_object(self, queryset = ...):
        return get_object_or_404(Lead, id = self.kwargs.get('lead_pk'))
    
    def get_success_url(self):
        return reverse_lazy('lead:lead_detail_url', args = [self.get_object().pk])


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

        