from django import forms
from .models import ServiceComment, BarberComment


class BarberCommentForm(forms.ModelForm):
    class Meta:
        model = BarberComment
        fields = ['stars', 'barber', 'text']



class ServiceCommentForm(forms.ModelForm):
    class Meta:
        model = ServiceComment
        fields = ['stars', 'service', 'text']      
