from rest_framework import routers
from .views import TestViewSet

router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
urlpatterns = router.urls
