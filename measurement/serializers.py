from rest_framework import serializers
from .models import Sensor, Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    """Сериализатор для измерений (вложенный в датчик)"""
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    """Сериализатор для списка датчиков (краткая информация)"""
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации по датчику (с измерениями)"""
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']