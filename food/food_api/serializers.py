from rest_framework import serializers
from .models import *

class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = "__all__"
        
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"