from main import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('research', views.research, name='research'),
    path('publications', views.publications, name='publications'),
    path('members', views.members, name='members'),
    path('alumni', views.alumni, name='alumni'),
    path('outreach', views.outreach, name='outreach'),
    path('funding', views.funding, name='funding'),
    path('calendar', views.calendar, name='calendar'),
    path('contact-us', views.contact_us, name='contact-us'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
