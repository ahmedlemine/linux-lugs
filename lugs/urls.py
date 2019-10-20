from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='lugs-home'),
    path('about/', views.about, name='lugs-about'),
]