# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include('addint.urls')),
    path("", include("app.urls")),  # add this
    path("", include('employee.urls')),
    path("", include('interview.urls')),
    
]
    