from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from multiselectfield import MultiSelectField


class BarberShopImage(models.Model):
    image = models.ImageField(upload_to='shop-image/')

    def __str__(self) -> str:
        return f'image {self.id}'
    


class BarberShop(models.Model):
    DAYS = (
        ('1', 'SATURDAY'),
        ('2', 'SUNDAY'),
        ('3', 'MONDAY'),
        ('4', 'TUESDAY'),
        ('5', 'WEDNESDAY'),
        ('6', 'THURSDAY'),
        ('7', 'FRIDAY'),
    )

    name = models.CharField(max_length=100) 
    description = models.TextField()

    images = models.ManyToManyField(BarberShopImage, related_name='barbershop')

    address = models.CharField(max_length=100)    
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(null=True, blank=True)
    instagaram_address = models.CharField(max_length=30, null=True, blank=True)

    working_days = MultiSelectField(choices=DAYS, verbose_name=_('working_days'))
    working_time = models.CharField(max_length=100, verbose_name=_('working_time'))

    def __str__(self) -> str:
        return f'{self.name}'
    
    

class Barber(models.Model):
    services = models.ManyToManyField('Service', related_name='barber')

    name = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=11)
    image = models.ImageField(upload_to='barbers-image/')

    active = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.name}'



class Service(models.Model):
    name_service = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='services-image/')

    active = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.name_service}'



class Reservation(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    created_add =models.DateTimeField(auto_now_add=True)



class ServiceComment(models.Model):
    STARS = (
        ('1', 'Awful'),
        ('2', 'Bad'),
        ('3', 'Normal'),        
        ('4', 'Good'),
        ('5', 'Perfect'),
    )
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    service = models.ForeignKey(Service, related_name='service_comment', on_delete=models.CASCADE, verbose_name=_('service'))
    stars = models.CharField(choices=STARS, max_length=1, verbose_name=_('stars'))
    text = models.TextField(verbose_name=_('text'))

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.service}'


class BarberComment(models.Model):
    STARS = (
        ('1', 'Awful'),
        ('2', 'Bad'),
        ('3', 'Normal'),        
        ('4', 'Good'),
        ('5', 'Perfect'),
    )
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    barber = models.ForeignKey(Barber, related_name='barber_comment', on_delete=models.CASCADE, verbose_name=_('barber'))
    stars = models.CharField(choices=STARS, max_length=1, verbose_name=_('stars'))
    text = models.TextField(verbose_name=_('text'))

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.barber}'
    