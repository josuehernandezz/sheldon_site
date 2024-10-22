from django.contrib import admin
from .models import CarouselImage, LabMember, Publication, GroupPhoto, ContentImage, Card, Funding, FundingImg, ResearchSection

# Register your models here.

admin.site.register(ContentImage)
admin.site.register(Publication)
admin.site.register(Card)
admin.site.register(GroupPhoto)
admin.site.register(Funding)
admin.site.register(FundingImg)
admin.site.register(ResearchSection)

class LabMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'year_joined', 'year_finished', 'position', 'is_alumni')
    list_filter = ('is_alumni', 'position', 'year_joined', 'year_finished')
    search_fields = ('name', 'email', 'bio')

admin.site.register(LabMember, LabMemberAdmin)


class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('display_instance', 'image', 'alt')
    search_fields = ('alt',)

    def display_instance(self, obj):
        return str(obj)  # or return obj.some_field to customize what you display
    display_instance.short_description = 'Carousel Image'  # Optional: Set a column header

admin.site.register(CarouselImage, CarouselImageAdmin)
# admin.site.register(CarouselImage)
