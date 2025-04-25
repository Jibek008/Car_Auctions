from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name']

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'




class CarModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    class Meta:
        model = Car
        fields = ['brand', 'car_model']


class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    car_model = CarModelSerializer()
    seller = UserProfileSerializer()
    class Meta:
        model = Car
        fields = '__all__'


class AuctionSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    class Meta:
        model = Auction
        fields = '__all__'


class AuctionListSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    class Meta:
        model = Auction
        fields = '__all__'

class AuctionDetailSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    class Meta:
        model = Auction
        fields = '__all__'



class BidListSerializer(serializers.ModelSerializer):
    auction = AuctionSerializer()
    buyer = UserProfileSerializer()
    class Meta:
        model = Bid
        fields = '__all__'


class BidDetailSerializer(serializers.ModelSerializer):
    auction = AuctionSerializer()
    buyer = UserProfileSerializer()
    class Meta:
        model = Bid
        fields = '__all__'



class FeedbackSerializer(serializers.ModelSerializer):
    seller = UserProfileSerializer()
    buyer = UserProfileSerializer()
    class Meta:
        model = Feedback
        fields = '__all__'