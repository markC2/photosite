from django.urls import path
from photos import views

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index')
]
