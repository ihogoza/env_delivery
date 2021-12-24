from django.db.models import fields
from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
    # title = serializers.CharField(max_length=100)
    # content = serializers.CharField()

    def validate(self, data):
        if data['m_manufacturedate'] > data['m_expirydate']:
            raise serializers.ValidationError("A medicine can't be expered before it is manufactured")
        return data

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['owner']

class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
