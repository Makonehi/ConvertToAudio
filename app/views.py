from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def indexAppView(request):
    return render(request, 'app/index.html')

class ContactAppView(TemplateView):
    template_name = 'app/contact.html'


class AboutAppView(TemplateView):
    template_name = 'app/about.html'
