"""calendar_app_dev URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("secret/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profile/", include("apps.profiles.urls")),
]

admin.site.site_header = "Calendar_APP Admin"
admin.site.site_title = "Calendar_APP Admin Portal"
admin.site.index_title = "Welcome to Calendar_APP Portal"
