from rest_framework import routers

from .views import CarViewSet


router = routers.DefaultRouter()
router.register("", CarViewSet)
urlpatterns = router.urls
