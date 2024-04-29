from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ServicesView(TemplateView):
    template_name = 'services.html'

class ProjectsView(TemplateView):
    template_name = 'projects.html'

class NewsView(TemplateView):
    template_name = 'news.html'

class FaqView(TemplateView):
    template_name = 'faq.html'

class ProductsView(TemplateView):
    template_name = 'products.html'

class OfferView(TemplateView):
        template_name = 'offer.html'

class ContactView(TemplateView):
     template_name = 'contact.html'