from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class Room(models.Model):
    host         = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    name         = models.CharField(max_length=200)
    description  = models.TextField(null=True, blank = True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated      = models.DateTimeField(auto_now=True)
    created      = models.DateTimeField(auto_now_add=True)
    image        = models.ImageField(blank=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    room    = models.ForeignKey(Room, on_delete=models.CASCADE)
    body    = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['updated','created']
    def __str__(self):
        return self.body[0:50]


class Carousel(models.Model):
    image       = models.ImageField(upload_to="pics/%y/%m/%d/")
    title       = models.CharField(max_length=150)
    link        = models.TextField(null=True, blank=True)
    sub_title   = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title       = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    genre       = models.CharField(max_length=150)
    cost        = models.IntegerField()
    image       = models.TextField()

class Pool(models.Model):
    # design = models.CharField(max_length=400, name='Дизайн')

    CHOICES = [
        ('1', 'Отвратительно'),
        ('2', 'Плохо'),
        ('3', 'Нормально'),
        ('4', 'Отлично'),
        ('5', 'Восхитительно'),
    ]
    design = models.CharField(max_length=400,
                              choices=CHOICES,
                              default="5")
    functionality = models.CharField(max_length=400,
                              choices=CHOICES,
                              default="5")
    creativity = models.CharField(max_length=400,
                              choices=CHOICES,
                              default="5")
    content = models.CharField(max_length=400,
                              choices=CHOICES,
                              default="5")

    other = models.TextField(max_length=500, blank=True)
    agreement = models.BooleanField('Согласие на получение рассылки',default=False)