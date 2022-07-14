"""
Definition of models.
"""

from django.db import models
from django.db.models.base import Model

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    jobs = models.ManyToManyField(Job, blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    primary_contact = models.CharField(max_length=100)
    jobs = models.ForeignKey(Job, on_delete=models.CASCADE)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

