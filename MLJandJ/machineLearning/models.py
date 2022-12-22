from uuid import uuid4

from django.db import models


class Car(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    mpg = models.FloatField()
    horsepower = models.FloatField()
