from django.db import models

# Create your models here.
class Hospital(models.Model):
    hosp_name = models.CharField(max_length=250, null=False, blank=False, default='')
    hosp_name_np = models.CharField(max_length=250, null=False, blank=False, default='')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.hosp_name