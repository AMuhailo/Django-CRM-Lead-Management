from django.urls import path
from . import views

app_name = 'agent'

urlpatterns = [
    path('', views.AgentListView.as_view(), name = 'agent_list_url'), 
    path('agent/<agent_pk>/detail/', views.AgentDetailView.as_view(), name = 'agent_detail_url'),
    path('agent/create/', views.AgentCreateView.as_view(), name = 'agent_create_url'),
    path('agent/<agent_pk>/update/', views.AgentUpdateView.as_view(), name = 'agent_update_url'),
]
