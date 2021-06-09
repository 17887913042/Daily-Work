from django.db import models

# Create your models here.

class Book(models.Model):

    id = models.AutoField(primary_key=True)  # 自增主键
    name = models.CharField(max_length=16)  # varchar(16)
    author = models.CharField(max_length=128)  # varchar(128)