# ccdj623/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
# from ninja.main import NinjaAPI
from ccdj623 import settings

# from .api import api


urlpatterns = [
    # path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('events/' , include('events.urls'))
    # path("api/", api.urls)
]

admin.site.site_header  =  "LOMB CMS Admin"
admin.site.site_title  =  "LOMB  Admin Site"
admin.site.index_title  = "LOMB  Admin Site"

if settings.DEBUG_TOOLBAR:
    from ccdj623.settings import DEBUG_TOOLBAR

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

