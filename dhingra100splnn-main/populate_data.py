from django.core.management.base import BaseCommand
from your_app_name.models import MySolarrr, solargeneration, Temperature, efficiency, Humidity, UV_Indexx, Irradiance
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populate the database with random data'

    def generate_random_data(self):
        return {
            'sales': random.randint(0, 1000),
            'revenue': random.randint(0, 50000),
            'invertor_power_conversion': random.randint(0, 1000),
            'faulty_panels': random.randint(0, 100),
            'working_panels': random.randint(0, 500),
            'weather_prediction': random.randint(0, 100),
            'maintainance_cost': random.randint(0, 10000),
            'Profit_and_loss': random.randint(-5000, 5000),
            'Rain_prediction': random.randint(0, 100),
            'Energy_Distribution': random.randint(0, 1000),
        }

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating data...")
        self.populate_mysolarrr()
        self.populate_other_models()
        self.stdout.write("Data populated successfully.")

    def populate_mysolarrr(self):
        for _ in range(100):  # Adjust the range for the number of records you want to create
            MySolarrr.objects.create(
                date=datetime.now() - timedelta(days=random.randint(0, 365)),
                **self.generate_random_data()
            )

    def populate_other_models(self):
        for model in [solargeneration, Temperature, efficiency, Humidity, UV_Indexx, Irradiance]:
            for _ in range(100):  # Adjust the range for the number of records you want to create
                model.objects.create(
                    date=datetime.now() - timedelta(days=random.randint(0, 365)),
                    **{f'_{hour}_00': random.uniform(0, 100) for hour in range(4, 21)}
                )
