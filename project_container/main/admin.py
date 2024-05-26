from django.contrib import admin
from .models import CarouselImage, LabMember

# Register your models here.

class MainAdminArea(admin.ModelAdmin):
    site_header = 'Administration'

# main_site = MainAdminArea()
# main_site.register(CarouselImage)

admin.site.register(CarouselImage, MainAdminArea)
admin.site.register(LabMember)
