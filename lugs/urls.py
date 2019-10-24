from django.urls import path
from .views import (LugListView, 
                    LugDetailView,
                    LugCreateView
                    )
from . import views

urlpatterns = [
    path('', LugListView.as_view(), name='lugs-home'),
    path('lug/<int:pk>/', LugDetailView.as_view(), name='lug-detail'),
    path('lug/new/', LugCreateView.as_view(), name='lug-create'),
    path('about/', views.about, name='lugs-about'),
]