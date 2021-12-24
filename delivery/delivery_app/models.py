from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Medicine(models.Model):
    m_name = models.CharField(max_length=50)
    m_price = models.DecimalField(max_digits=13, decimal_places=3)
    m_description = models.TextField()
    m_quantity = models.CharField(max_length=50)
    m_manufacturedate = models.DateField()
    m_expirydate = models.DateField()
    in_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.m_name


class Order(models.Model):
    product = models.ManyToManyField(Medicine)
    quantity = models.IntegerField()
    address = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=13, decimal_places=3)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    





