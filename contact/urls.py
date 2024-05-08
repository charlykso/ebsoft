from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.contact, name='contact'),
    path('<str:pk>/get/', views.contact_detail, name='contact_detail'),
    path('apply/', views.apply, name='apply'),
    path('status', views.get_status, name='status'),
]
