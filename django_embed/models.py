from django.db import models

class SeaSurfaceTemperature(models.Model):
    time = models.DateTimeField(blank=True, null=False, primary_key=True)
    temperature = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sea_surface_temperature'
        
class Mastedata(models.Model):
    index = models.BigIntegerField(blank=True, null=False, primary_key=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    lat_long_g = models.BooleanField(blank=True, null=True)
    lat_long_m = models.BooleanField(blank=True, null=True)
    lat_long_b = models.BooleanField(blank=True, null=True)
    difference_meter = models.FloatField(blank=True, null=True)
    link = models.BigIntegerField(blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    source_of_error = models.TextField(blank=True, null=True)
    commissioning_year = models.BigIntegerField(blank=True, null=True)
    fill_color = models.TextField(blank=True, null=True)
    line_color = models.TextField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    size = models.BigIntegerField(blank=True, null=True)
    line_width = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mastedata'
