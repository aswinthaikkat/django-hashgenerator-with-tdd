from django.db import models

# Create your models here.


class Hash(models.Model):
    name = models.TextField()
    encoding = models.CharField(max_length=64)

    def __str__(self):
        return self.name
