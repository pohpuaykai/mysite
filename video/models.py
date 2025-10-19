from django.db import models

class Audio(models.Model):
    data = models.BinaryField()
    tag = models.TextField()