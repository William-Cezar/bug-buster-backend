from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_bug, name='report_bug'),
]
