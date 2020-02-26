from django.db import models
from datetime import time

class Campus(models.Model):
   campus_id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100)
   description = models.CharField(max_length=500, default='This campus is associate to the whole DCU Campus')

   def __str__(self):
      return self.name

class Restaurant(models.Model):
   restaurant_id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   campus_id = models.ForeignKey(Campus,on_delete = models.CASCADE)
   opening_hours = models.TimeField()
   closing_hours = models.TimeField()
   capacity = models.IntegerField()
   staff_only = models.BooleanField(default=False)
   week_end_open = models.BooleanField(default=False)
   week_end_opening_hours = models.TimeField(default=time(0,0))
   week_end_closing_hours = models.TimeField(default=time(0,0))