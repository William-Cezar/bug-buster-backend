from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_bug, name='report_bug'),
    path('api/login/', views.user_login, name='login'), 
    path('api/logout/', views.user_logout, name='logout'),
]
