from django.urls import path

from . import views

app_name = 'vacantes'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]