from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_bug, name='report_bug'),
    path('login/', views.user_login, name='login'), 
    path('logout/', views.user_logout, name='logout'),
    path('is_authenticated/', views.is_authenticated, name='is_authenticated'),
]
