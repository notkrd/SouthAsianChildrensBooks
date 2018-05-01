from django.db import models

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default="")
    publisher = models.CharField(max_length=200, default="")
    comments = models.TextField(default="")

    def __str__(self):
        return self.title

