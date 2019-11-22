from django.db import models

# Create your models here.
class Classmate(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    roll = models.IntegerField(max_length=100)

    def __str__(self):
        return self.firstname