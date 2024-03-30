from django.contrib import admin
from django.conf.urls.static import static
from django.http import HttpResponse
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from . import settings

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to CatchUp API", content_type="text/plain")),
    path('admin/', admin.site.urls),
    path("api/", include("products.urls")),
    path("api/", include("scrapers.urls")),
    path("api/", include("testing.urls")),
    path('api/auth/', include('authentication.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
