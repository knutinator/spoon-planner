from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.validators import RangeMinValueValidator
from django.contrib.postgres.validators import RangeMaxValueValidator
from psycopg2.extras import NumericRange
from django.utils import timezone


class Task(models.Model):
    # associates the task with the user that created it.
    # If a user is deleted, also deletes all their created tasks
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    energy = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=5)
    completed = models.BooleanField(default=False)
    selected = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['completed', '-created_at']


class DailyEnergy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_energy = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
