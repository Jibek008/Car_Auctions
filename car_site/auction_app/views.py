from .serializers import *
from rest_framework import viewsets,generics


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class BrandListAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer


class BrandDetailAPIView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class AuctionListAPIView(generics.ListAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionListSerializer


class AuctionDetailAPIView(generics.RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

class BidListAPIView(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidListSerializer

class BidDetailAPIView(generics.RetrieveAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidDetailSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


