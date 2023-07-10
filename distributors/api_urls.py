from django.urls import path
from .api_views import *


urlpatterns = [
    # Users
    path('user/create/', UserCreate.as_view(), name='DistributorsCreateListUser'),
    path('user/list/', UserList.as_view(), name='DistributorsListUser'),
    path('user/update/<str:email>', UserUpdate.as_view(), name='DistributorsUpdateUser'),
    path('user/detail/<str:email>', UserDetail.as_view(), name='DistributorsDetailUser'),
    # Products
    path('product/create/', UserCreate.as_view(), name='DistributorsCreateListProduct'),
    path('product/list/', UserList.as_view(), name='DistributorsListProduct'),
    path('product/update/<str:serial>/', UserUpdate.as_view(), name='DistributorsUpdateProduct'),
    path('product/destroy/<str:email>/', UserUpdate.as_view(), name='DistributorsUpdateProduct'),
    path('product/detail/', ProductDetail.as_view(), name='DistributorsDetailProduct')
]