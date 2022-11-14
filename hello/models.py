from django.db import models


class Helloer(models.Model):
    Name = models.CharField(max_legnth=255)
