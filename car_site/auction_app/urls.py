from tkinter.font import names

from rest_framework import routers
from .views import *
from django.urls import path,include

router = routers.SimpleRouter()
router.register(r'user',UserProfileViewSet,basename='user_list')
router.register(r'car_model',CarModelViewSet,basename='car_model_list')
router.register(r'car',CarViewSet,basename='car_list')
router.register(r'feedback',FeedbackViewSet,basename='feedback_List')


urlpatterns = [
     path('',include(router.urls)),
     path('brand/', BrandListAPIView.as_view(), name='brand_list'),
     path('brand/<int:pk>/', BidDetailAPIView.as_view(), name='brand_detail'),
     path('auction/', AuctionListAPIView.as_view(), name='auction_list'),
     path('auction/<int:pk>/', AuctionDetailAPIView.as_view(), name='auction_detail'),
     path('bid/', BidListAPIView.as_view(), name='bid_list'),
     path('bid/<int:pk>/', BidDetailAPIView.as_view(), name='bid_detail'),
]