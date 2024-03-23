from django.urls import path
from photos import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index')
]


urlpatterns += staticfiles_urlpatterns()