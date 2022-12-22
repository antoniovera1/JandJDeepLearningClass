from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'uuid',
            'mpg',
            'horsepower',
        )


class HorsePowerSerializer(serializers.Serializer):
    horse_power = serializers.FloatField()
