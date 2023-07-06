from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexAppView, name='home'),
    path('contact/', views.ContactAppView.as_view(), name='contact'),
    path('about/', views.AboutAppView.as_view(), name='about'),
]



