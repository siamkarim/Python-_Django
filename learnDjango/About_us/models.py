from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class teacher(models.Model):
    tid = models.IntegerField()
    tname = models.CharField(max_length =40)
    tmail = models.EmailField(max_length =30 )