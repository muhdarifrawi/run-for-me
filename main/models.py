from django.db import models

# Create your models here.
class orders(models.Model):
    sku = models.CharField(max_length=100, blank=False)
    request = models.TextField(blank=False)
    cost = models.IntegerField(blank=False)
    image = models.ImageField(blank=True, null=True)
    post_date = models.DateField(blank=False, null=False)
    due_date = models.DateField(blank=False, null=False)
    
    def __str__(self):
        return self.sku
        
class showOrders(models.Model):
    orders = models.ForeignKey("main.orders", on_delete=models.CASCADE)
    owner = models.ForeignKey("accounts.MyUser", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.orders.sku + " : " + str(self.owner)
        
    