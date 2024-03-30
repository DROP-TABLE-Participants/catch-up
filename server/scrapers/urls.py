from rest_framework import routers
from .views import ScraperViewSet

router = routers.DefaultRouter()
router.register('scrapers', ScraperViewSet, basename='scrapers')
urlpatterns = router.urls
