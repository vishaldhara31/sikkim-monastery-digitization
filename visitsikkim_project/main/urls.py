from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.index, name="index"),
    path('archives/', views.archives, name="archives"),
    path('tour/', views.tour, name="tour"),
    path('interactive/', views.interactive, name="interactive"),
    path('manuscripts/', views.manuscripts, name="manuscripts"),
    path('murals/', views.murals, name="murals"),
    path('book/',views.book, name='book'),
    path('travel/',views.travel, name='travel'),
    path('about/',views.about, name='about'),
    path('events/', views.events, name = 'events'),



    # --- User Authentication URLs ---
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    # --- Other Pages ---
    path('cultural/', views.cultural_calendar, name='cultural_calendar'),

]
