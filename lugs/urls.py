from django.urls import path
from .views import (LugListView, 
                    LugDetailView,
                    # LugCreateView,
                    # LugUpdateView,
                    LugDeleteView,
                    LugsByUserListView,
                    MyLugsListView,
                    LugsByCityListView,
                    )
from . import views

urlpatterns = [
    path('', LugListView, name='lugs-home'),
    # path('', LugListView.as_view(), name='lugs-home'),
    path('lugs-by/<str:username>/', LugsByUserListView.as_view(), name='lugs-by-user'),
    path('my-lugs/', MyLugsListView.as_view(), name='my-lugs'),
    path('lug/<slug:slug>/', LugDetailView.as_view(), name='lug-detail'),
    # path('new-lug/', LugCreateView.as_view(), name='lug-create'),
    # path('lug/<slug:slug>/update', LugUpdateView.as_view(), name='lug-update'),
    path('lug/<slug:slug>/delete', LugDeleteView.as_view(), name='lug-delete'),
    path('lugs-in-city/<int:city_id>/', LugsByCityListView.as_view(), name='lugs-by-city'),
    path('about/', views.about, name='lugs-about'),
    path('join-lug/<slug:slug>/', views.joinLug, name='join-lug'),
    path('leave-lug/<slug:slug>/', views.leaveLug, name='leave-lug'),
    path('lug-members/<slug:slug>/', views.lugMembersView, name='lug-members'),
    path('create_lug/', views.createLug, name='lug-create'),
    path('edit_lug/<slug:slug>/', views.editLug, name='lug-update')
]