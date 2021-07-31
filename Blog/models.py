from django.db import models
from datetime import date
# Create your models here.

#To POST AN ARTICLE
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc=models.TextField()
    date_created=models.CharField(max_length=20)
    created_by=models.CharField(max_length=20)


