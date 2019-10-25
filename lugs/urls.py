from django.urls import path
from .views import (LugListView, 
                    LugDetailView,
                    LugCreateView,
                    LugUpdateView,
                    LugDeleteView,
                    LugsByUserListView
                    )
from . import views

urlpatterns = [
    path('', LugListView.as_view(), name='lugs-home'),
    path('user/<str:username>/', LugsByUserListView.as_view(), name='lugs-by-user'),
    path('lug/<int:pk>/', LugDetailView.as_view(), name='lug-detail'),
    path('lug/new/', LugCreateView.as_view(), name='lug-create'),
    path('lug/<int:pk>/update', LugUpdateView.as_view(), name='lug-update'),
    path('lug/<int:pk>/delete', LugDeleteView.as_view(), name='lug-delete'),
    path('about/', views.about, name='lugs-about'),
]