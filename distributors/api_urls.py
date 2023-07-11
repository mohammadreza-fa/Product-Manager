from django.urls import path
from .api_views import *


urlpatterns = [
    # Users
    path('user/list/', UserList.as_view(), name='DistributorsListUser'),
    path('user/create/', UserCreate.as_view(), name='DistributorsCreateListUser'),
    path('user/update/<str:email>/', UserUpdate.as_view(), name='DistributorsUpdateUser'),
    path('user/detail/<str:email>/', UserDetail.as_view(), name='DistributorsDetailUser'),
    # Products
    path('product/list/', ProductList.as_view(), name='DistributorsListProduct'),
    path('product/create/', ProductCreate.as_view(), name='DistributorsCreateProduct'),
    path('product/update/<serial__serial>/', ProductUpdate.as_view(), name='DistributorsUpdateProduct'),
    path('product/detail/<serial__serial>/', ProductDetail.as_view(), name='DistributorsDetailProduct'),
    path('product/destroy/<serial__serial>/', ProductDestroy.as_view(), name='DistributorsUpdateProduct'),
    # Properties
    path('property/list/', ProductList.as_view(), name='DistributorsListProperty'),
    path('property/detail/<serial__serial>/', ProductDetail.as_view(), name='DistributorsDetailProperty'),
    # Email
    path('email/create/', EmailCreate.as_view(), name='DistributorsCreateEmail'),
]
