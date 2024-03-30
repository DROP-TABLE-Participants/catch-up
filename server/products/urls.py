from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
urlpatterns = router.urls