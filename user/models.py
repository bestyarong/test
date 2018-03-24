from django.db import models

class User(models.Model):
    SEX = (
        ('M', '男'),
        ('F', '女'),
        ('U', '保密'),
    )

    nickname = models.CharField(max_length=64, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    icon = models.ImageField()
    age = models.IntegerField()
    sex = models.CharField(max_length=8, choices=SEX)
