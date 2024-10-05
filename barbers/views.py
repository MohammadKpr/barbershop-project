from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import *


def home_page(request):
    barber_shop = BarberShop.objects.get(name='BARBER')
    pictures = barber_shop.images.all()
    return render(request, 'home_page.html', {'barber_shop' : barber_shop, 'pictures' : pictures})



def service_page(request):
    services = Service.objects.filter(active=True)
    form = ServiceCommentForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.customer = request.user
        form.save()
        return redirect('service_page')

    return render(request, 'service.html', {"services" : services, 'form' : form})



def barber_page(request):
    barbers = Barber.objects.filter(active=True)
    form = BarberCommentForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.customer = request.user
        form.save()
        return redirect('barber_page')

    return render(request, 'barber.html', {"barbers" : barbers, 'form' : form})



def barber_details(request, pk):
    barber = Barber.objects.get(pk=pk)
    barber_comments = barber.barber_comment.all()
    context = {
        'barber_comments': barber_comments,
        'barber' : barber,
    }
    return render(request, 'barber_detail.html', context=context)



def service_details(request, pk):
    service = Service.objects.get(pk=pk)
    service_comments = service.service_comment.all()
    context = {
        'service_comments': service_comments,
        'service' : service,
    }
    return render(request, 'service_detail.html', context=context)