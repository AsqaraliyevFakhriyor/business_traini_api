from django.contrib import admin

from .models import ApplicationModel


@admin.register(ApplicationModel)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["username", "phone_number",
                    "email", "business_type", "created", "visited"]
    list_filter = ('created', "visited")
    search_fields = ("username", "phone_number", "business_type", "email")
    date_hierarchy = 'created'
    ordering = ('-created',)
