from django.db import models

class BroneTime(models.Model):
    time = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.time}'

class Place(models.Model):
    number = models.CharField(max_length = 10)
    device_id = models.CharField(max_length = 100)
    status = models.CharField(max_length = 10 , default = 'free')

    def __str__(self):
        return f'Parking place {self.number}'

class PlaceBrone(models.Model):
    placenumber = models.ForeignKey(Place, on_delete= models.CASCADE,blank=True,null=True)
    bronetime = models.ForeignKey(BroneTime, on_delete=models.CASCADE, blank=True, null=True)