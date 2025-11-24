from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.URLField()

    def _str_(self):
        return self.name