from django.contrib import admin
from . import models

admin.site.register(models.Fruit)
admin.site.register(models.Vegetable)
admin.site.register(models.Classification)
admin.site.register(models.FruitByClass)
admin.site.register(models.VegetableByClass)
