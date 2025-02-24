from django.urls import path
from . import views

app_name = 'lead'

urlpatterns = [
    path('', views.LeadListView.as_view(), name = 'lead_list_url'), 
    path('<lead_pk>/detail/', views.LeadDetailView.as_view(), name = 'lead_detail_url'),
    path('create/', views.LeadCreateView.as_view(), name = 'lead_create_url'),
    path('<lead_pk>/update/', views.LeadUpdateView.as_view(), name = 'lead_update_url'),
    path('<lead_pk>/delete/', views.LeadDeleteView.as_view(), name = 'lead_delete_url'),
    path('unassigned/<lead_pk>/lead/', views.AssignLeadAgent.as_view(), name = 'assign_lead_url'),
    path('category/',views.CategoryListView.as_view(), name = 'category_list_url'),
    path('category/<category_title>/',views.CategoryDetailView.as_view(), name = 'category_detail_url'),
    path('<lead_pk>/category/update/',views.CategoryLeadUpdateView.as_view(), name = 'category_lead_update_url')
]
