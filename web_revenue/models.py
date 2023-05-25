from django.db import models
from django.contrib.auth.models import User


class CityGroups(models.TextChoices):
    BIG = 'B', ('Big city')
    OTHER = 'O', ('Other')

class RestTypes(models.TextChoices): 
    FC = 'FC', ('FC')
    IL = 'IL', ('IL')
    DT = 'DT', ('DT')
    MB = 'MB', ('MB')

class RestaurantData(models.Model):
    id = models.IntegerField(
        unique=True, 
        verbose_name="Your unique rest id",
        primary_key=True,
        )
    open_date = models.DateField()
    city = models.CharField(max_length=50)
    city_group = models.CharField(max_length=1, choices=CityGroups.choices)
    type = models.CharField(max_length=2, choices=RestTypes.choices)
    revenue = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True, default=0)
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to='./web_app_files')
    uploaded_at = models.DateTimeField(auto_now_add=True)