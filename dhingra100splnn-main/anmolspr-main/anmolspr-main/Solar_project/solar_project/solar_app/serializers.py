from rest_framework import serializers
from solar_app.models import MySolarrr,solargeneration,Temperature,efficiency,Humidity,Performance,UV_Indexx,Production,Irradiance

class EnergyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySolarrr
        fields = '__all__'



class MySolarrrSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySolarrr
        fields = '__all__'



class UV_IndexxSerializer(serializers.ModelSerializer):
    class Meta:
        model = UV_Indexx
        fields = '__all__'


class IrradianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Irradiance
        fields = '__all__'



class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = '__all__'



class efficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = efficiency
        fields = '__all__'



class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'


class solargenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = solargeneration
        fields = '__all__'



