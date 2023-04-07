from django.db import models
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
from psycopg2.extras import NumericRange

# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

#     def __str__(self):
#         return f"{self.name} ({self.age})"

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
#    energy = models.CharField(max_length=2, choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')))
    energy = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=5)

    def __str__(self):
        return f"{self.name} - {self.description} ({self.energy} spoons)"
