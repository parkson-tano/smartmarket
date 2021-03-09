from django.db import models
from django.contrib.auth.models import User
# Create your models here.

REGION = (
    ('Adamawa', 'Adamawa'),
    ('Central', 'Central'),
    ('East', 'East'),
    ('Far North', 'Far North'),
    ('Littoral', 'Littoral'),
    ('North', 'North'),
    ('Northwest', 'Northwest'),
    ('South', 'South'),
    ('Southwest', 'Southwest'),
    ('West', 'West')
)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length = 250)
    region = models.CharField(max_length=20, choices=REGION)
    town = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
