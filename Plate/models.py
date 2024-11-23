from django.db import models

class Vehicle(models.Model):
    number_plate = models.CharField(max_length=20)
    num_img = models.ImageField() 

    def __str__(self):
        return self.number_plate
