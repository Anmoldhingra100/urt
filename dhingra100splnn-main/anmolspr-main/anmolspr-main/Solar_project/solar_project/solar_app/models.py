from django.db.models import Sum
from django.utils import timezone
from django.db.models.functions import TruncWeek
from django.db import models
from datetime import timedelta


class MySolarrr(models.Model):
    date = models.DateField(default=timezone.now)
    sales = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)
    invertor_power_conversion = models.IntegerField(default=0)
    faulty_panels = models.IntegerField(default=0)
    working_panels = models.IntegerField(default=0)
    weather_prediction = models.IntegerField(default=0)
    maintainance_cost = models.IntegerField(default=0)
    Profit_and_loss = models.IntegerField(default=0)
    Rain_prediction = models.IntegerField(default=0)
    Energy_Distribution = models.IntegerField(default=0)
    



class solargeneration(models.Model):

    date = models.DateField()
    _04_00 = models.IntegerField(default=0)
    _05_00 = models.IntegerField(default=0)
    _06_00 = models.IntegerField(default=0)
    _07_00 = models.IntegerField(default=0)
    _08_00 = models.IntegerField(default=0)
    _09_00 = models.IntegerField(default=0)
    _10_00 = models.IntegerField(default=0)
    _11_00 = models.IntegerField(default=0)
    _12_00 = models.IntegerField(default=0)
    _13_00 = models.IntegerField(default=0)
    _14_00 = models.IntegerField(default=0)
    _15_00 = models.IntegerField(default=0)
    _16_00 = models.IntegerField(default=0)
    _17_00 = models.IntegerField(default=0)
    _18_00 = models.IntegerField(default=0)
    _19_00 = models.IntegerField(default=0)
    _20_00 = models.IntegerField(default=0)




class Production(models.Model):

    date = models.DateField()
    _04_00 = models.IntegerField(default=0)
    _05_00 = models.IntegerField(default=0)
    _06_00 = models.IntegerField(default=0)
    _07_00 = models.IntegerField(default=0)
    _08_00 = models.IntegerField(default=0)
    _09_00 = models.IntegerField(default=0)
    _10_00 = models.IntegerField(default=0)
    _11_00 = models.IntegerField(default=0)
    _12_00 = models.IntegerField(default=0)
    _13_00 = models.IntegerField(default=0)
    _14_00 = models.IntegerField(default=0)
    _15_00 = models.IntegerField(default=0)
    _16_00 = models.IntegerField(default=0)
    _17_00 = models.IntegerField(default=0)
    _18_00 = models.IntegerField(default=0)
    _19_00 = models.IntegerField(default=0)
    _20_00 = models.IntegerField(default=0)


class Performance(models.Model):

    date = models.DateField()
    _04_00 = models.IntegerField(default=0)
    _05_00 = models.IntegerField(default=0)
    _06_00 = models.IntegerField(default=0)
    _07_00 = models.IntegerField(default=0)
    _08_00 = models.IntegerField(default=0)
    _09_00 = models.IntegerField(default=0)
    _10_00 = models.IntegerField(default=0)
    _11_00 = models.IntegerField(default=0)
    _12_00 = models.IntegerField(default=0)
    _13_00 = models.IntegerField(default=0)
    _14_00 = models.IntegerField(default=0)
    _15_00 = models.IntegerField(default=0)
    _16_00 = models.IntegerField(default=0)
    _17_00 = models.IntegerField(default=0)
    _18_00 = models.IntegerField(default=0)
    _19_00 = models.IntegerField(default=0)
    _20_00 = models.IntegerField(default=0)

class Temperature(models.Model):

    date = models.DateField()
    _04_00 = models.IntegerField(default=0)
    _05_00 = models.IntegerField(default=0)
    _06_00 = models.IntegerField(default=0)
    _07_00 = models.IntegerField(default=0)
    _08_00 = models.IntegerField(default=0)
    _09_00 = models.IntegerField(default=0)
    _10_00 = models.IntegerField(default=0)
    _11_00 = models.IntegerField(default=0)
    _12_00 = models.IntegerField(default=0)
    _13_00 = models.IntegerField(default=0)
    _14_00 = models.IntegerField(default=0)
    _15_00 = models.IntegerField(default=0)
    _16_00 = models.IntegerField(default=0)
    _17_00 = models.IntegerField(default=0)
    _18_00 = models.IntegerField(default=0)
    _19_00 = models.IntegerField(default=0)
    _20_00 = models.IntegerField(default=0)
    



class Humidity(models.Model):

    date = models.DateField()
    _04_00 = models.IntegerField(default=0)
    _05_00 = models.IntegerField(default=0)
    _06_00 = models.IntegerField(default=0)
    _07_00 = models.IntegerField(default=0)
    _08_00 = models.IntegerField(default=0)
    _09_00 = models.IntegerField(default=0)
    _10_00 = models.IntegerField(default=0)
    _11_00 = models.IntegerField(default=0)
    _12_00 = models.IntegerField(default=0)
    _13_00 = models.IntegerField(default=0)
    _14_00 = models.IntegerField(default=0)
    _15_00 = models.IntegerField(default=0)
    _16_00 = models.IntegerField(default=0)
    _17_00 = models.IntegerField(default=0)
    _18_00 = models.IntegerField(default=0)
    _19_00 = models.IntegerField(default=0)
    _20_00 = models.IntegerField(default=0)




class efficiency(models.Model):

    date = models.DateField()
    _04_00 = models.IntegerField(default=0)
    _05_00 = models.IntegerField(default=0)
    _06_00 = models.IntegerField(default=0)
    _07_00 = models.IntegerField(default=0)
    _08_00 = models.IntegerField(default=0)
    _09_00 = models.IntegerField(default=0)
    _10_00 = models.IntegerField(default=0)
    _11_00 = models.IntegerField(default=0)
    _12_00 = models.IntegerField(default=0)
    _13_00 = models.IntegerField(default=0)
    _14_00 = models.IntegerField(default=0)
    _15_00 = models.IntegerField(default=0)
    _16_00 = models.IntegerField(default=0)
    _17_00 = models.IntegerField(default=0)
    _18_00 = models.IntegerField(default=0)
    _19_00 = models.IntegerField(default=0)
    _20_00 = models.IntegerField(default=0)
    



class UV_Indexx(models.Model):

    date = models.DateField()
    _04_00 = models.IntegerField(default=0)
    _05_00 = models.IntegerField(default=0)
    _06_00 = models.IntegerField(default=0)
    _07_00 = models.IntegerField(default=0)
    _08_00 = models.IntegerField(default=0)
    _09_00 = models.IntegerField(default=0)
    _10_00 = models.IntegerField(default=0)
    _11_00 = models.IntegerField(default=0)
    _12_00 = models.IntegerField(default=0)
    _13_00 = models.IntegerField(default=0)
    _14_00 = models.IntegerField(default=0)
    _15_00 = models.IntegerField(default=0)
    _16_00 = models.IntegerField(default=0)
    _17_00 = models.IntegerField(default=0)
    _18_00 = models.IntegerField(default=0)
    _19_00 = models.IntegerField(default=0)
    _20_00 = models.IntegerField(default=0)

    


class Irradiance(models.Model):

    date = models.DateField()
    _04_00 = models.IntegerField(default=0)
    _05_00 = models.IntegerField(default=0)
    _06_00 = models.IntegerField(default=0)
    _07_00 = models.IntegerField(default=0)
    _08_00 = models.IntegerField(default=0)
    _09_00 = models.IntegerField(default=0)
    _10_00 = models.IntegerField(default=0)
    _11_00 = models.IntegerField(default=0)
    _12_00 = models.IntegerField(default=0)
    _13_00 = models.IntegerField(default=0)
    _14_00 = models.IntegerField(default=0)
    _15_00 = models.IntegerField(default=0)
    _16_00 = models.IntegerField(default=0)
    _17_00 = models.IntegerField(default=0)
    _18_00 = models.IntegerField(default=0)
    _19_00 = models.IntegerField(default=0)
    _20_00 = models.IntegerField(default=0)
    
    