from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
from psycopg2.extras import NumericRange


class Task(models.Model):
    # associates the task with the user that created it. If a user is deleted, also deletes all their created task
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    energy = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=5)
    completed = models.BooleanField(default=False)
    selected = models.BooleanField(default=False)
