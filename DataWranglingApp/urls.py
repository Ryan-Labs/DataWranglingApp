from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('airlines/', views.airlines, name='airlines'),
    path('top/', views.top, name='top'),
]