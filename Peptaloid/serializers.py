# alkaloid_app/serializers.py

from rest_framework import serializers
from .models import Peptaloid

class PeptaloidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peptaloid
        fields = '__all__'