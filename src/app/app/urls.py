"""
app URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns: list[URLPattern | URLResolver] = [
    path("admin/", admin.site.urls),
    path("api/core/", include("core.urls")),
    path("api/user/", include("user.urls")),
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
            path("api/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),
        ]
    )
