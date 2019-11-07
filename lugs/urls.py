from django.urls import path
from .views import (LugListView, 
                    LugDetailView,
                    LugCreateView,
                    LugUpdateView,
                    LugDeleteView,
                    LugsByUserListView,
                    MyLugsListView,
                    LugsByCityListView,
                    LugsByCountryListView,
                    )
from . import views

urlpatterns = [
    path('', LugListView.as_view(), name='lugs-home'),
    path('lugs-by/<str:username>/', LugsByUserListView.as_view(), name='lugs-by-user'),
    path('my-lugs/', MyLugsListView.as_view(), name='my-lugs'),
    path('lug/<slug:slug>/', LugDetailView.as_view(), name='lug-detail'),
    path('new-lug/', LugCreateView.as_view(), name='lug-create'),
    path('lug/<slug:slug>/update', LugUpdateView.as_view(), name='lug-update'),
    path('lug/<slug:slug>/delete', LugDeleteView.as_view(), name='lug-delete'),
    path('lugs-in-city/<str:city>/', LugsByCityListView.as_view(), name='lugs-by-city'),
    path('lugs-in-country/<str:country>/', LugsByCountryListView.as_view(), name='lugs-by-country'),    
    path('about/', views.about, name='lugs-about'),
    path('join-lug/<slug:slug>/', views.joinLug, name='join-lug'),
    path('leave-lug/<slug:slug>/', views.leaveLug, name='leave-lug'),
    path('lug-members/<slug:slug>/', views.lugMembersView, name='lug-members')
]