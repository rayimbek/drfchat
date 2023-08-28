from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Club(models.Model):
    user = models.ForeignKey(User, verbose_name='User' ,null=True, on_delete=models.CASCADE)
    name = models.CharField('Club name', max_length=120)
    description = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null = True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name
