from django.urls import path
from .api_views import *


urlpatterns = [
    # Users
    path('user/detail/', UserDetail.as_view(), name='CustomerDetailUser'),
    # Products
    path('product/detail/<serial__serial>/', ProductDetail.as_view(), name='CustomerDetailProduct'),
    path('product/list/', ProductList.as_view(), name='CustomerListProduct'),
]