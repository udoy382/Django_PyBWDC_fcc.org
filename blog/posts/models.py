from django.db import models
from datetime import datetime

# Create your models here.

# ----------------------------------------------

# Admin Panel
# Username = Udoy
# Email = srudoy436@gmail.com
# password = srudoy2299

# ----------------------------------------------


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(), blank=True)