from django.contrib import admin
from .models import Category, EmissionFactor, Activity

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'color']

@admin.register(EmissionFactor)
class EmissionFactorAdmin(admin.ModelAdmin):
    list_display = ['activity_name', 'category', 'co2_per_unit', 'unit']
    list_filter = ['category']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'emission_factor', 'quantity', 'date', 'total_emissions']
    list_filter = ['user', 'category', 'date']
    search_fields = ['notes']
