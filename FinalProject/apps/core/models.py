from django.db import models

class Vegetable(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=10000, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Fruit(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=10000, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Classification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class VegetableByClass(models.Model):
    vegetable = models.ForeignKey(Vegetable, on_delete=models.CASCADE)
    Class = models.ForeignKey(Classification, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.Class}: {self.vegetable}"

class FruitByClass(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    Class = models.ForeignKey(Classification, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.Class}: {self.fruit}"