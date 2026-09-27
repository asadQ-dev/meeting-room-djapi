from rest_framework import routers  # type: ignore[reportMissingImports]
from .views import BookingViewSet, RoomViewSet

router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = router.urls