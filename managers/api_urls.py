from django.urls import path
from .api_views import *


urlpatterns = [
    # Users
    path('user/list/', UserList.as_view(), name='ManagerListUser'),
    path('user/create/', UserCreate.as_view(), name='ManagerCreateUser'),
    path('user/update/<str:email>/', UserUpdate.as_view(), name='ManagerUpdateUser'),
    path('user/detail/<str:email>/', UserDetail.as_view(), name='ManagerDetailUser'),
    path('user/destroy/<str:email>/', UserDestroy.as_view(), name='ManagerDestroyUser'),
    # Products
    path('product/list/', ProductList.as_view(), name='ManagerListProduct'),
    path('product/create/', ProductCreate.as_view(), name='ManagerCreateProduct'),
    path('product/update/<str:serial>/', ProductUpdate.as_view(), name='ManagerUpdateProduct'),
    path('product/detail/<str:serial>/', ProductDetail.as_view(), name='ManagerDetailProduct'),
    path('product/destroy/<str:serial>/', ProductDestroy.as_view(), name='ManagerDestroyProduct'),
    # Serials
    path('serial/list/', SerialList.as_view(), name='ManagerListSerial'),
    path('serial/update/<str:serial>/', SerialUpdate.as_view(), name='ManagerUpdateSerial'),
    path('serial/destroy/<str:serial>/', SerialDestroy.as_view(), name='ManagerDestroySerial'),
    path('serial/detail/<serial__serial>/', SerialDetail.as_view(), name='ManagerDetailSerial'),
    # Properties
    path('property/create/', PropertyCreate.as_view(), name='ManagerCreateProperty'),
    path('property/list/', PropertyList.as_view(), name='ManagerListPropertyAll'),
    path('property/list/paid/', PropertyListPaid.as_view(), name='ManagerListPropertyPaid'),
    path('property/list/unpaid/', PropertyListUnpaid.as_view(), name='ManagerListPropertyUnpaid'),
    path('property/update/<int:id>/', PropertyUpdate.as_view(), name='ManagerUpdatePropertyID'),
    path('property/detail/<int:id>/', PropertyDetail.as_view(), name='ManagerDetailPropertyID'),
    path('property/destroy/<int:id>/', PropertyDestroy.as_view(), name='ManagerDestroyPropertyID'),
    path('property/update/<str:serial>/', PropertyUpdateSerial.as_view(), name='ManagerUpdatePropertySerial'),
    path('property/destroy/<str:serial>/', PropertyDestroySerial.as_view(), name='ManagerDestroyPropertySerial'),
    path('property/detail/<serial__serial>/', PropertyDetailSerial.as_view(), name='ManagerDetailPropertySerial'),
]
