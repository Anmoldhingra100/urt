from django.contrib import admin
from .models import MySolarrr,solargeneration,Temperature,efficiency,Humidity,Performance,UV_Indexx,Production,Irradiance

class solarAdmin(admin.ModelAdmin):
    list_display = ['date','sales','revenue','invertor_power_conversion','faulty_panels','working_panels','weather_prediction','maintainance_cost','Profit_and_loss','Rain_prediction','Energy_Distribution']  # Fields to display in the list view
     # Fields to display in the list view
    
admin.site.register(MySolarrr, solarAdmin)




class solargenerationadmin(admin.ModelAdmin):
    
    list_display = ['date','_04_00','_05_00','_06_00','_07_00','_08_00','_09_00','_10_00','_11_00','_12_00','_13_00','_14_00','_15_00','_16_00','_17_00','_18_00','_19_00','_20_00']

    
admin.site.register(solargeneration, solargenerationadmin)



class UV_IndexxAdmin(admin.ModelAdmin):
    
    list_display = ['date','_04_00','_05_00','_06_00','_07_00','_08_00','_09_00','_10_00','_11_00','_12_00','_13_00','_14_00','_15_00','_16_00','_17_00','_18_00','_19_00','_20_00']

    
admin.site.register(UV_Indexx, UV_IndexxAdmin)





class IrradianceAdmin(admin.ModelAdmin):
    
    list_display = ['date','_04_00','_05_00','_06_00','_07_00','_08_00','_09_00','_10_00','_11_00','_12_00','_13_00','_14_00','_15_00','_16_00','_17_00','_18_00','_19_00','_20_00']

    
admin.site.register(Irradiance, IrradianceAdmin)



class efficiencyadmin(admin.ModelAdmin):
    
    list_display = ['date','_04_00','_05_00','_06_00','_07_00','_08_00','_09_00','_10_00','_11_00','_12_00','_13_00','_14_00','_15_00','_16_00','_17_00','_18_00','_19_00','_20_00']

    
admin.site.register(efficiency, efficiencyadmin)


class HumidityAdmin(admin.ModelAdmin):
    
    list_display = ['date','_04_00','_05_00','_06_00','_07_00','_08_00','_09_00','_10_00','_11_00','_12_00','_13_00','_14_00','_15_00','_16_00','_17_00','_18_00','_19_00','_20_00']

    
admin.site.register(Humidity, HumidityAdmin)

class TemperatureAdmin(admin.ModelAdmin):
    
    list_display = ['date','_04_00','_05_00','_06_00','_07_00','_08_00','_09_00','_10_00','_11_00','_12_00','_13_00','_14_00','_15_00','_16_00','_17_00','_18_00','_19_00','_20_00']

    
admin.site.register(Temperature, TemperatureAdmin)














