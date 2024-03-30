from rest_framework import routers
from .views import ScraperViewSet, HistoryViewSet

router = routers.DefaultRouter()
router.register('scrapers', ScraperViewSet, basename='scrapers')
router.register('history', HistoryViewSet, basename='history')
urlpatterns = router.urls
