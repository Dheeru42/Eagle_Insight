from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Vehicle(models.Model):
    vid = models.AutoField(primary_key=True,default=None)
    number_plate = models.CharField(max_length=20)
    num_img = models.ImageField()
    date = models.DateField(default=now)
    time = models.TimeField(default=now)
    

    def __str__(self):
        return self.number_plate
