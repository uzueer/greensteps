from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_activity, name='add_activity'),
    path('delete/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('analytics/', views.analytics, name='analytics'),
    path('api/emission-factors/', views.get_emission_factors, name='get_emission_factors'),
]
