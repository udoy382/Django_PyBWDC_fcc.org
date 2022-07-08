from django.db import models
from django.db.models.base import Model


# ---------------------------------------------

# Admin Panel
# Username = Udoy
# Email_address = srudoy436@gmail.com
# password = udoy436

# -----------------------------------------------
# Create your models here.

class Feature(models.Model):
    # id = int
    # name = str
    # content = str
    # is_true = bool


    # -----------New Model---------

    name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.name