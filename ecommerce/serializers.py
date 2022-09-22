from rest_framework import serializers
from .models import Orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'product_name', 'product_price', 'product_description', 'product_date', 'product_time')
