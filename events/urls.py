from django.urls import path
from . import views


app_name = 'events'

urlpatterns = [
    path('new', views.EventView.as_view(), name='new'),

]