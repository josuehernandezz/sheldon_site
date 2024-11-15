from page_visits import views
from django.urls import path

urlpatterns = [
    path('', views.page_visits, name='page_visits'),
]
