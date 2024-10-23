from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import CarouselImage, LabMember, Publication, GroupPhoto, ContentImage, Card, Funding, FundingImg, ResearchSection

# Register your models here.

class MyAdminSite(AdminSite):
    site_header = "Sheldon Group Admin"
    site_title = "Sheldon Group"
    index_title = "Welcome to the Admin Page"

admin_site = MyAdminSite(name='Sheldon Group')

# 1 Card Admin View

class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'alt', 'image')
    list_filter = ('title', 'description', 'alt')

admin_site.register(Card, CardAdmin)

# 2 Carousel Admin View

class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('display_instance', 'image', 'alt')
    search_fields = ('alt',)

    def display_instance(self, obj):
        return str(obj)  # or return obj.some_field to customize what you display
    display_instance.short_description = 'Carousel Image'  # Optional: Set a column header

admin_site.register(CarouselImage, CarouselImageAdmin)

# 3 ContentImage Admin View

class ContentImageAdmin(admin.ModelAdmin):
    list_display = ('alt', 'image')

admin_site.register(ContentImage, ContentImageAdmin)

# 4 FundingImage Admin View

class FundingImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin_site.register(FundingImg, FundingImageAdmin)

# 5 Funding Admin View

class FundingAdmin(admin.ModelAdmin):
    list_display = ('name', 'funding_source')
    list_filter = ('name', 'funding_source')
    search_fields = ('name', 'funding_source')

admin_site.register(Funding, FundingAdmin)

# 6 Group Photo Admin View

class GroupPhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin_site.register(GroupPhoto, GroupPhotoAdmin)

# 7 Lab Member Admin View

class LabMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'year_joined', 'year_finished', 'position', 'is_alumni')
    list_filter = ('is_alumni', 'position', 'year_joined', 'year_finished')
    search_fields = ('name', 'email', 'bio')

admin_site.register(LabMember, LabMemberAdmin)

# 8 Publication Admin View

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('publication_number', 'name', 'title', 'authors', 'journal', 'year', 'url')
    list_filter = ('year', 'journal')
    search_fields = ('name', 'title', 'journal')

admin_site.register(Publication, PublicationAdmin)

# 9 Research Section Admin View

class ResearchSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'research_summary')
    search_fields = ('title',)

admin_site.register(ResearchSection, ResearchSectionAdmin)
