from rest_framework import serializers
from .models import Contact, UserAplication

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class UserAplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAplication
        fields = '__all__'