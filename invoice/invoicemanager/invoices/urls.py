from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice-details', InvoiceDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/invoices/', views.InvoiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='invoice-list'),
    path('api/invoices/<int:pk>/', views.InvoiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='invoice-detail'),

]



