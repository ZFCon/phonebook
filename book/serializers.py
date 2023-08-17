from rest_framework import serializers
from .models import Contact, PhoneNumber

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
