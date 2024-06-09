from django.db import models
from django.contrib.auth.models import User
from bidding_systems.util.enums import symbols, forcing_types

class CustomBidCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class BidSystem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)
    query_objects = CustomBidCategoryManager()

class BidCategory(models.Model):
    bid_system_id = models.ForeignKey(BidSystem, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    query_objects = CustomBidCategoryManager()

class BidSituation(models.Model):
    bid_category_id = models.ForeignKey(BidCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    sequences = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    query_objects = CustomBidCategoryManager()

class Bid(models.Model):
    bid_situation_id = models.ForeignKey(BidSituation, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=4, choices=symbols)
    name = models.CharField(blank=True, max_length=100, default='')    
    forcing_type = models.CharField(blank=True, max_length=9, choices=forcing_types)
    strength = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True)
    is_alerted = models.BooleanField()
    query_objects = CustomBidCategoryManager()
