from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.URLField()
    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username
