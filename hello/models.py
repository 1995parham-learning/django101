from django.db import models


class Helloer(models.Model):
    """
    Helloers are the persons that wants to say hello
    """

    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    age = models.IntegerField()
