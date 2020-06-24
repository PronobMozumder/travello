from django.db import models

class destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)


class info(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Adderss = models.CharField(max_length=100)