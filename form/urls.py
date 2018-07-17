from django.urls import path

from . import views

app_name = 'form'
urlpatterns = [
    path('', views.get_name, name='form'),
 #   path('', views.post_list, name='delete'),
]