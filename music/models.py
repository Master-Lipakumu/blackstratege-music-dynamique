from django.db import models
from django.urls import reverse

# Create your models here.

class Video(models.Model):
    URL = models.URLField()

    def __str__(self):
        return self.URL




class Contact(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=100)
    messages = models.TextField()

    def __str__(self):
        return self.nom, self.messages