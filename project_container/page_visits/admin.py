from django.contrib import admin
from main.admin import admin_site
from .models import PageVisit
from django.db import models
from django.utils import timezone

# Register your models here.

class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('url', 'formatted_visited_at', 'ip_address', 'user_agent', 'referer', 'visit_count')

    def formatted_visited_at(self, obj):
        # Convert to local time using timezone.localtime
        local_time = timezone.localtime(obj.visited_at)
        return local_time.strftime('%b %d, %Y - %I:%M %p')  # Example: 'Nov 12, 2024 - 03:00 PM'
    
    formatted_visited_at.admin_order_field = 'visited_at'  # Allows ordering by visited_at
    formatted_visited_at.short_description = 'Visited At'  # Customize column name

admin_site.register(PageVisit, PageVisitAdmin)
