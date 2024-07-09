from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vendor_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'vendors', views.VendorViewSet)
router.register(r'purchase_orders', views.PurchaseOrderViewSet)
router.register(r'historical_performance', views.HistoricalPerformanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
