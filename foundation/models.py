from django.db import models

class Ticket(models.Model):
    responseContent = models.BinaryField(null=True, blank=True)