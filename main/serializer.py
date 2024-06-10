from rest_framework import serializers
from .models import Alcance

class AlcanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcance
        fields = '__all__'