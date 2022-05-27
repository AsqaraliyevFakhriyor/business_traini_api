from django.contrib import admin

from .models import ApplicationModel

# Register your models here.

@admin.register(ApplicationModel)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["username", "phone_number", "business_type", "created"]
    list_filter = ('created', 'business_type',)
    search_fields = ("username", "phone_number", "business_type")
    date_hierarchy = 'created'
    ordering = ('created',)
