from django.views.generic import TemplateView



class AboutUsView(TemplateView):
    template_name = 'aboutus.html'