from django.db import models
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
from psycopg2.extras import NumericRange


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    energy = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=5)

    def __str__(self):
        return f"{self.name} - {self.description} ({self.energy} spoons)"
