from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.db.models.functions import TruncWeek
from solar_app.models import MySolarrr,solargeneration,Temperature,efficiency,Humidity,Performance,UV_Indexx,Production,Irradiance
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta
from solar_app.models import MySolarrr
from .serializers import EnergyDataSerializer
from django.utils import timezone
from .serializers import MySolarrrSerializer,HumiditySerializer,solargenerationSerializer,TemperatureSerializer,efficiencySerializer,PerformanceSerializer,UV_IndexxSerializer,ProductionSerializer,IrradianceSerializer
from rest_framework import viewsets

from .serializers import MySolarrrSerializer




def home_page_view(request):
    return request(request,'solarr.html')



class WeeklyDataAPIView(APIView):
    def get(self, request):
        today = timezone.now()
        start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week
        end_of_week = start_of_week + timedelta(days=6)  # Sunday of the current week

        # Querying the database for records within the current week
        weekly_data = MySolarrr.objects.filter(date__range=[start_of_week, end_of_week])
        serializer = EnergyDataSerializer(weekly_data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)







class RecordsLastSevenDaysView(APIView):
    def get(self, request, *args, **kwargs):
        now = timezone.now()
        seven_days_ago = now - timedelta(days=7)  # Changed to 7 days as the class name suggests

        # Query all models
        solarrr_records = MySolarrr.objects.filter(date__gte=seven_days_ago, date__lte=now)
        irradiance_records = Irradiance.objects.filter(date__gte=seven_days_ago, date__lte=now)
        humidity_records = Humidity.objects.filter(date__gte=seven_days_ago, date__lte=now)
        efficiency_records = efficiency.objects.filter(date__gte=seven_days_ago, date__lte=now)
        temperature_records = Temperature.objects.filter(date__gte=seven_days_ago, date__lte=now)
        performance_records = Performance.objects.filter(date__gte=seven_days_ago, date__lte=now)
        uv_indexx_records = UV_Indexx.objects.filter(date__gte=seven_days_ago, date__lte=now)
        solar_generation_records = solargeneration.objects.filter(date__gte=seven_days_ago, date__lte=now)
        production_records = Production.objects.filter(date__gte=seven_days_ago, date__lte=now)

        # Serialize the data
        data = {
            'solarrr': MySolarrrSerializer(solarrr_records, many=True).data,
            'irradiance': IrradianceSerializer(irradiance_records, many=True).data,
            'humidity': HumiditySerializer(humidity_records, many=True).data,
            'efficiency': efficiencySerializer(efficiency_records, many=True).data,
            'temperature': TemperatureSerializer(temperature_records, many=True).data,
            'performance': PerformanceSerializer(performance_records, many=True).data,
            'uv_indexx': UV_IndexxSerializer(uv_indexx_records, many=True).data,
            'solar_generation': solargenerationSerializer(solar_generation_records, many=True).data,
            'production': ProductionSerializer(production_records, many=True).data,
        }

        return Response(data, status=status.HTTP_200_OK)









