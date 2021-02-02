from django.db import models

'''
    makemigrations  ->  model --> migration.py 
    migrate --> database --> apply 
    
'''
# Create your models here.
class flight(models.Model):
    origin=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    duration=models.IntegerField()

    def __str__(self):
        return f"flight({self.origin}-{self.destination})"
'''
object 
fl1=flight(origin='ahm',destination='baroda',duration=2323)
fl1.save()
'''

