
from django.contrib import admin
from django.urls import path
from . import views
from django_prometheus import exports

urlpatterns = [
    path('', views.home, name='home'),  # отобразит 'web/index.html'
    path("metrics/", exports.ExportToDjangoView, name="metrics"),
    path('slow/', views.slow_view, name='home'),
    path('usual/', views.usual_view, name='usual'),
    path('random/', views.random_view, name='random'),
]