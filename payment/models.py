from django.db import models
from accounts.models import MyUser

# Create your models here.
class orders(models.Model):
    sku = models.CharField(max_length=100, blank=False)
    full_name = models.CharField(max_length=100, blank=False)
    full_address = models.CharField(max_length=150, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    contact = models.CharField(max_length=8, blank=False, null=True)
    run_request = models.TextField(blank=False)
    cost = models.IntegerField(blank=False, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    post_date = models.DateField(auto_now_add=True,blank=False)
    due_date = models.DateField(blank=False, null=False)
    requester = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    urgency = models.ForeignKey("Urgency", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.sku
        
class Urgency(models.Model):
    urgency_tag = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.urgency_tag