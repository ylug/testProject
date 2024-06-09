from django.urls import include, path
from rest_framework.routers import DefaultRouter
from supplier.views import SupplierViewSet
from supplier.apps import SupplyersConfig

app_name = SupplyersConfig.name

supplyers_router = DefaultRouter()
supplyers_router.register(r'supplyers', SupplierViewSet, basename='supplyers')

urlpatterns = [
    path('', include(supplyers_router.urls)),
]
