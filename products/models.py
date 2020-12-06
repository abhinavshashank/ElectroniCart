from django.db import models
from django.conf import settings
from .storages import ProtectedStorage
User = settings.AUTH_USER_MODEL



# Create your models here.
class Product(models.Model):
    #id = models.AutoField()
    user = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='products/', null=True, blank=True, default=None)
    media = models.FileField(upload_to='products/', storage=ProtectedStorage,default=None)
    title = models.CharField(max_length = 220, default=None)
    content = models.TextField(null = True, blank = True, default=None)
    price = models.DecimalField(max_digits = 10, decimal_places=2, default = 0.00)
    inventory = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)


    def has_inventory(self):
        return self.inventory > 0

    def remocve_item_from_inventory(self, count = 1, save=True):
        current_inv = self.inventory
        current_inv -= count
        self.inventory = current_inv
        if save == True:
            self.save()
        return self.inventory