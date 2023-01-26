from django.contrib.auth.models import User
from django.db import models

from .testM import getcovid


# Create your models here.

class Custumer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sexe = models.CharField(max_length=10)
    age = models.IntegerField()
    PhoneNumbers = models.CharField(max_length=20)
    #image = models.ImageField(upload_to='images')

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='envoyeur')
    text = models.TextField()
    lien = models.CharField(max_length=200)
    receive= models.ForeignKey(User, on_delete=models.CASCADE,  related_name='recepteur')
    date_sender = models.DateTimeField(auto_now_add=True, blank=True)

class Malaria(models.Model):
    #nom_m = models.CharField(max_length=200)
    symptomes = models.CharField(max_length=200)
    #user = models.ForeignKey(Custumer,on_delete=models.CASCADE)
class Palu(models.Model):
    nom_p = models.CharField(max_length=200)

class Avc(models.Model):
    nom_a = models.CharField(max_length=200)

class Malaria_m(models.Model):
    nom_ma = models.CharField(max_length=200)
    symptome = models.CharField(max_length=200)
    #user = models.ForeignKey(Custumer,on_delete=models.CASCADE)


class Prediction(models.Model):
    nom_patient = models.CharField(max_length=200)
    maladie = models.CharField(max_length=200)
    probabilite = models.FloatField()

class GetMalaria(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    malaria = models.ForeignKey(Prediction, on_delete=models.CASCADE)