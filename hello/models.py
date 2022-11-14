from django.db import models


class Helloer(models.Model):
    name = models.CharField(max_legnth=255)
    family = models.CharField(max_length=255)
    age = models.IntegerField()
