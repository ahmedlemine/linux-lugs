from django.urls import path
from .views import (LugDeleteView,
                    LugsByUserListView,
                    MyLugsListView,
                    LugsByCityListView,
                    )
from . import views

urlpatterns = [
    path('', views.lugListView, name='lugs-home'),
    path('lugs-by/<str:username>/', LugsByUserListView.as_view(), name='lugs-by-user'),
    path('my-lugs/', MyLugsListView.as_view(), name='my-lugs'),
    path('lug/<str:slug>/', views.lugDetailView, name='lug-detail'),
    path('lug/<str:slug>/delete', LugDeleteView.as_view(), name='lug-delete'),
    path('lugs-in-city/<int:city_id>/', LugsByCityListView.as_view(), name='lugs-by-city'),
    path('find-lugs-in-city/', views.findLugByCityView, name='find-lugs-in-city'),
    path('search-lugs/', views.searchLUGsView, name='search-lugs'),
    path('about/', views.about, name='lugs-about'),
    path('join-lug/<str:slug>/', views.joinLug, name='join-lug'),
    path('leave-lug/<str:slug>/', views.leaveLug, name='leave-lug'),
    path('lug-members/<str:slug>/', views.lugMembersView, name='lug-members'),
    path('create_lug/', views.createLug, name='lug-create'),
    path('edit_lug/<str:slug>/', views.editLug, name='lug-update'),
    path('lug/<str:slug>/create_post', views.createPost, name='create-post'),
    path('lug/edit_post/<int:pk>/', views.editPost, name='edit-post'),
    path('lug/delete_post/<int:pk>/', views.deletePost, name='delete-post'),
    path('lug/<str:slug>/posts', views.lugPostsListView, name='lug-posts'),
    path('lug/post/<int:pk>', views.lugPostDetail, name='post-detail'),
    path('api/lug_list/', views.lug_list, name='api-lug-list'),
    path('api/city_list/', views.city_list, name='api-city-list'),
]