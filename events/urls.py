from django.urls import path
from . import views
from .models import EventFeed


app_name = 'events'

urlpatterns = [
    path('new', views.EventView.as_view(), name='new'),
    path('latest/feed.ics', EventFeed()),
]