from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('services/', service_page, name='service_page'),
    path('barbers/', barber_page, name='barber_page'),

    path('barber/<int:pk>', barber_details, name='barber_detail'),
    path('service/<int:pk>', service_details, name='service_detail'),
]
