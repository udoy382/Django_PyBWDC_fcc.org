from django.db import models

# Create your models here.

# ----------------------------------
# admin panel
# username = Udoy
# email = srudoy436@gmail.com
# password = srudoy2299


# username = srudoy
# password = srudoy22
# ----------------------------------

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    date_enrolled = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name