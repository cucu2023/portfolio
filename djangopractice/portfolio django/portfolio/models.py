"""from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import imageField

class Project(models.Model):
    title = CharField(max_lenght=100)
    description = CharField(max_lenght=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = Urlfield(blank=True)
"""
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)
