from django.urls import path
from .views import ItemListCreate, ItemDetail, XAccountView


urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('x-account/', XAccountView.as_view(), name='x account'),
]
