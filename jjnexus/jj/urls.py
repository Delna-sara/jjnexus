from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.home, name='home'),
    # path('services/', views.services, name='services'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('contact/', contact_view, name='contact'),
]
