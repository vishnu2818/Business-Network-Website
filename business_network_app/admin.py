from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'is_approved', 'created_at')  # Columns displayed in the admin list view
    list_filter = ('is_approved',)  # Add a filter sidebar for 'status'
    search_fields = ('email',)  # Add a search bar for 'name' and 'created_by'
    ordering = ('is_approved', 'email')  # Default ordering in the admin list view

admin.site.register(Company, CompanyAdmin)