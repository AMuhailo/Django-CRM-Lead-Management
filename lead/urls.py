from django.urls import path
from . import views

app_name = 'lead'

urlpatterns = [
    path('', views.LeadListView.as_view(), name = 'lead_list_url'), 
    path('lead/<lead_pk>/detail/', views.LeadDetailView.as_view(), name = 'lead_detail_url'),
    path('lead/create/', views.LeadCreateView.as_view(), name = 'lead_create_url'),
    path('lead/<lead_pk>/update/', views.LeadUpdateView.as_view(), name = 'lead_update_url'),
]
