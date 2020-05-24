from pathlib import Path

from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

import bokeh
from bokeh.server.django import autoload, directory, document, static_extensions

from . import views

bokeh_app_config = apps.get_app_config('bokeh.server.django')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sea_surface/", views.sea_surface),
]

base_path = settings.BASE_PATH


bokeh_apps = [
    autoload("sea_surface", views.sea_surface_handler),
    document("bokeh_apps/sea_surface", base_path / "bokeh_apps" / "sea_surface.py"),
]

urlpatterns += static_extensions()
urlpatterns += staticfiles_urlpatterns()
