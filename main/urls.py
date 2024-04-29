from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('services', views.ServicesView.as_view(), name='services'),
    path('projects', views.ProjectsView.as_view(), name='projects'),
    path('news', views.NewsView.as_view(), name='news'),
    path('faq', views.FaqView.as_view(), name='faq'),
    path('products', views.ProductsView.as_view(), name='products'),
    path('offer', views.OfferView.as_view(), name='offer'),
    path('contact', views.ContactView.as_view(), name='contact'),
]