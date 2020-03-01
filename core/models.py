from django.db import models

# Create your models here.
# Create your models here.
class Item(models.Model):
    type_of_food = models.CharField(max_length=100)
    exp_date = models.DateTimeField('expiration date')

    def __str__(self):
        return self.type_of_food

class Category(models.Model):
    vegi=models.ForeignKey(Item, on_delete=models.CASCADE)
   # meat=models.Charfield(max_length=100)