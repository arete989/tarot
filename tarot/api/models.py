from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=100, default='')
    explanation = models.TextField()
