from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, CategoryViewSet, MenuItemViewSet, BookingViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'menu', MenuItemViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
]