from django.db import models
from django.contrib.auth.models import User


class CityGroups(models.TextChoices):
    BIG = 'Big Cities', ('Big Cities')
    OTHER = 'Other', ('Other')

class RestTypes(models.TextChoices): 
    FC = 'FC', ('FC')
    IL = 'IL', ('IL')
    DT = 'DT', ('DT')
    MB = 'MB', ('MB')

class PNParameter(models.Model):
    Id = models.IntegerField(
        unique=True, 
        verbose_name="Your unique rest id",
        primary_key=True,
        )
    P1  = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P2  = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P3  = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P4  = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P5  = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P6  = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P7  = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P8  = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P9  = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P10 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P11 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P12 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P13 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P14 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P15 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P16 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P17 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P18 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P19 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P20 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P21 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P22 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P23 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P24 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P25 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P26 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P27 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P28 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P29 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P30 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P31 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P32 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P33 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P34 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P35 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P36 = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    P37 = models.DecimalField(max_digits=3, decimal_places=1, default=0)


class RestaurantData(PNParameter):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    Open_Date = models.DateField()
    City = models.CharField(max_length=50)
    City_Group = models.CharField(max_length=10, choices=CityGroups.choices)
    Type = models.CharField(max_length=2, choices=RestTypes.choices)
    revenue = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True, default=0)
    

class UploadedFile(models.Model):
    file = models.FileField(upload_to='./web_app_files')
    uploaded_at = models.DateTimeField(auto_now_add=True)